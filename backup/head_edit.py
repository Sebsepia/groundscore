from bs4 import BeautifulSoup
import os
import bs4

formatter = bs4.formatter.HTMLFormatter(indent=2)

def get_html_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def overwrite_head_content(html_file_path, new_head_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find the head element
    head_element = soup.find('head')

    # Check if head element exists
    if head_element:
        # Load the new content from the specified HTML file
        new_head_content = get_html_content(new_head_file_path)

        # Clear the existing content in the head
        head_element.clear()

        # Parse the new head content
        new_content_soup = BeautifulSoup(new_head_content, 'html.parser')

        # Append each tag from the new content to the head
        for tag in new_content_soup.find_all(recursive=False):
            head_element.append(tag)

        # Save the modified content back to the file with proper indentation
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify(formatter=formatter))
    else:
        print(f"Warning: No <head> element found in {html_file_path}")

def overwrite_head_in_directory(directory_path, new_head_file_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".html"):
            html_file_path = os.path.join(directory_path, filename)
            overwrite_head_content(html_file_path, new_head_file_path)
            print(f"Overwrote head content in {html_file_path}")

# Replace 'your_directory_path' with the path to your HTML files
directory_path = '.'

# Replace 'your_new_head_file.html' with the path to your new head content HTML file
new_head_file_path = 'script_html/head.html'
overwrite_head_in_directory(directory_path, new_head_file_path)