from bs4 import BeautifulSoup
import bs4
import os

formatter = bs4.formatter.HTMLFormatter(indent=2)

def get_html_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def update_nav_content(html_file_path, new_nav_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')


    # Find the nav element
    nav_element = soup.find('nav')

    # Check if nav element exists
    if nav_element:
        # Exclude image sources
        for img_tag in nav_element.find_all('img'):
            img_tag.extract()

        # Load the new content from the specified HTML file
        new_nav_content = get_html_content(new_nav_file_path)

        # Replace the content of the nav element with the new content
        nav_element.clear()
        nav_element.append(BeautifulSoup(new_nav_content, 'html.parser'))

        # Save the modified content back to the file with proper indentation
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify(formatter=formatter))
    else:
        print(f"Warning: No <nav> element found in {html_file_path}")


def update_nav_in_directory(directory_path, new_nav_file_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".html"):
            html_file_path = os.path.join(directory_path, filename)
            update_nav_content(html_file_path, new_nav_file_path)
            print(f"Updated nav content in {html_file_path}")

def process_html_file(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Get the base name of the HTML file (excluding extension)
        base_name = os.path.splitext(os.path.basename(html_file_path))[0]

        # Find all image tags in the HTML file
        img_tags = soup.find_all('img')

        # Process each image tag
        for img_tag in img_tags:
            src = img_tag.get('src')
            if src and base_name in src:
                # Update the 'src' attribute with the modified filename
                img_tag['src'] = src.replace(base_name, f"{base_name}_s")

    # Write the modified HTML content back to the file
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify(formatter=formatter)))

def process_html_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.html'):
            html_file_path = os.path.join(directory_path, filename)
            process_html_file(html_file_path)
            print(f"Processed: {filename}")

# Replace 'your_directory_path' with the path to your HTML files
directory_path = '.'

# Replace 'your_new_nav_file.html' with the path to your new nav content HTML file
new_nav_file_path = 'navigation.html'
update_nav_in_directory(directory_path, new_nav_file_path)
process_html_files(directory_path)