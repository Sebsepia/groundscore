# import os
# import sqlite3
# from jinja2 import Environment, Template, FileSystemLoader

# # Connect to SQLite database
# conn = sqlite3.connect("db.sqlite3")
# cursor = conn.cursor()

# # Fetch data from the zblog table
# cursor.execute('SELECT * FROM zblog_post WHERE sketchbook_category_id IS NOT NULL AND sketchbook_category_id != ""')
# zblog_rows = cursor.fetchall()

# # Close the database connection
# conn.close()

# # Load Jinja2 template
# env = Environment(loader=FileSystemLoader('.'))  # You may need to adjust the loader path
# template = env.get_template('template.html')

# # Generate HTML pages
# for zblog_row in zblog_rows:
#     # Extract blog details
#     id, post_date, slug, title, title_tag, portfolio_category_id, sketchbook_category_id = zblog_row[:7]

#     # Connect to SQLite database for related images
#     conn = sqlite3.connect('db.sqlite3')
#     cursor = conn.cursor()

#     # Fetch related blog images
#     cursor.execute('SELECT b_img, b_img_resize, b_img_alt, b_img_description, b_img_paragraph FROM zblog_blogimage WHERE postimg_id = ?', (id,))
#     blog_images = [{'b_img': row[0], 'b_img_resize': row[1],  'b_img_alt': row[2], 'b_img_description': row[3], 'b_img_paragraph': row[4]} for row in cursor.fetchall()]

#     cursor.execute('SELECT object_id, tag_id FROM taggit_taggeditem WHERE object_id = ?', (id,))
#     id_tags = [{'tag_id': row[1]} for row in cursor.fetchall()]

#     # Your first list
#     tag_id_list = id_tags

#     cursor.execute('SELECT * FROM taggit_tag')
#     name_tags = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]

#     # Create a mapping dictionary
#     tag_id_to_name = {tag['id']: tag['name'] for tag in name_tags}

#     # Transform the first list
#     tag_list = [{'tag_name': tag_id_to_name[tag['tag_id']]} for tag in id_tags]

#     # Render the HTML template with the data
#     html_content = template.render(post_date=post_date, title=title, slug=slug, blog_images=blog_images, tag_list=tag_list)

#     # Create folder based on sketchbook_category_id if it doesn't exist
#     folder_path = os.path.join('dump', str(sketchbook_category_id))
#     os.makedirs(folder_path, exist_ok=True)

#     # Save the HTML content to a file within the folder (you can customize the file name)
#     with open(os.path.join(folder_path, f'{slug.lower().replace(" ", "_")}.html'), 'w') as html_file:
#         html_file.write(html_content)

import os
import sqlite3
from jinja2 import Environment, FileSystemLoader

# Connect to SQLite database
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Fetch data from the zblog table
cursor.execute('SELECT * FROM zblog_post WHERE sketchbook_category_id IS NOT NULL AND sketchbook_category_id != ""')
zblog_rows = cursor.fetchall()

# Close the database connection
conn.close()

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'))  # You may need to adjust the loader path
template = env.get_template('template.html')

# Generate a single text file with all image paths for each subfolder
for zblog_row in zblog_rows:
    # Extract blog details
    id, _, _, _, _, _, sketchbook_category_id = zblog_row[:7]

    # Connect to SQLite database for related images
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Fetch related blog images
    cursor.execute('SELECT b_img FROM zblog_blogimage WHERE postimg_id = ?', (id,))
    blog_images = [row[0] for row in cursor.fetchall()]

    # Close the database connection
    conn.close()

    # Create folder based on sketchbook_category_id if it doesn't exist
    folder_path = os.path.join('dump', str(sketchbook_category_id))
    os.makedirs(folder_path, exist_ok=True)

    # Write all image paths to a text file
    txt_file_path = os.path.join(folder_path, 'image_paths.txt')
    with open(txt_file_path, 'w') as image_file:
        for image_path in blog_images:
            image_file.write(image_path + '\n')
