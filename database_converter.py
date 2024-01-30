
import os
import sqlite3
from jinja2 import Environment, Template, FileSystemLoader

# Connect to SQLite database
conn = sqlite3.connect("db.sqlite3");
cursor = conn.cursor()


# Fetch data from the zblog table
cursor.execute('SELECT * FROM zblog_post')
zblog_rows = cursor.fetchall()

# Close the database connection
conn.close()

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')



# Generate HTML pages
for zblog_row in zblog_rows:
    if len(zblog_row) >= 3:
        # Extract blog details
        id, post_date, slug, title, title_tag, portfolio_category_id, sketchbook_category_id = zblog_row[:7]
        print(post_date)

        # Connect to SQLite database for related images
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Fetch related blog images
        cursor.execute('SELECT b_img, b_img_resize, b_img_alt, b_img_description, b_img_paragraph FROM zblog_blogimage WHERE postimg_id = ?', (id,))
        blog_images = [{'b_img': row[0], 'b_img_resize': row[1],  'b_img_alt': row[2], 'b_img_description': row[3], 'b_img_paragraph': row[4] } for row in cursor.fetchall()]

        cursor.execute('SELECT object_id, tag_id FROM taggit_taggeditem WHERE object_id = ?', (id,))
        id_tags = [{'tag_id': row[1] } for row in cursor.fetchall()]

        


        # Your first list
        tag_id_list = id_tags

        cursor.execute('SELECT * FROM taggit_tag')
        name_tags = [{'id': row[0], 'name': row[1] } for row in cursor.fetchall()]

        # Create a mapping dictionary
        tag_id_to_name = {tag['id']: tag['name'] for tag in name_tags}

        # Transform the first list
        tag_list = [{'tag_name': tag_id_to_name[tag['tag_id']]} for tag in id_tags]



        # Render the HTML template with the data
        html_content = template.render(post_date=post_date, title=title, slug=slug, blog_images=blog_images, tag_list=tag_list,)

        # Save the HTML content to a file (you can customize the file name)
        filename = f'dump/{post_date}_{slug.lower().replace(" ", "_")}.html'
        with open(filename, 'w') as html_file:
            html_file.write(html_content)



# # Retrieve data from the "zblog_post" table
# cursor.execute('''
#     SELECT p.id, p.post_date, p.slug, p.title, b.b_img
#     FROM zblog_post p
#     LEFT JOIN zblog_blogimage b ON p.id = b.postimg_id
# ''')
# posts = cursor.fetchall()

# if len(zblog_row) >= 3:
#         # Extract blog details
#         id, post_date, slug, title, title_tag, portfolio_category_id, sketchbook_category_id = zblog_row[:7]

#         # Connect to SQLite database for related images
#         conn = sqlite3.connect('db.sqlite3')
#         cursor = conn.cursor()

     
# # Close the database connection
# conn.close()

# # for post in posts:
# #     id, post_date, slug, title, b_img = post
# #     print(id, b_img)
    

# # Iterate over the posts and create HTML files
# for post in posts:
#     id, post_date, slug, title, b_img = post

#     # HTML template using Jinja2
#     html_template = Template("""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>{{ title }}</title>
#         <p>{{id}}</p>
#     </head>
#     <body>
#         <h1>{{ title }}</h1>
#         {% for id in post %}
#         <p>{{id}}</p>
#         {% endfor %}        

#     </body>
#     </html>
#     """)

#     # Render the template with post data
#     html_content = html_template.render(title=title)

#     # Save HTML file
#     file_path = os.path.join('dump', f'{slug}.html')
#     with open(file_path, 'w') as html_file:
#         html_file.write(html_content)
