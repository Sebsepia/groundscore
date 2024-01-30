import os
from bs4 import BeautifulSoup

def extract_image_paths(html_file):
    with open(html_file, 'r', encoding='utf-8', errors='replace') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Adjust the CSS selector based on how your image paths are structured in your HTML
        img_elements = soup.select('img[src]')
        return [img['src'] for img in img_elements]

def generate_image_paths_txt(folder_path):
    html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]

    all_image_paths = []

    for html_file in html_files:
        html_path = os.path.join(folder_path, html_file)
        image_paths = extract_image_paths(html_path)
        all_image_paths.extend(image_paths)

    # Write all image paths to a text file
    txt_file_path = os.path.join(folder_path, 'all_image_paths.txt')
    with open(txt_file_path, 'w') as image_file:
        for image_path in all_image_paths:
            image_file.write(image_path + '\n')

if __name__ == "__main__":
    # Specify the root folder containing subfolders with HTML files
    root_folder = 'sketchbooks/'

    # Process each subfolder
    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)
        if os.path.isdir(subfolder_path):
            generate_image_paths_txt(subfolder_path)