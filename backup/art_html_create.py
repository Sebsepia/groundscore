import os
from PIL import Image

def resize_image(image_path, max_dimension):
    img = Image.open(image_path)
    original_width, original_height = img.size

    if original_width > max_dimension or original_height > max_dimension:
        aspect_ratio = original_width / original_height
        if original_width > original_height:
            new_width = max_dimension
            new_height = int(max_dimension / aspect_ratio)
        else:
            new_height = max_dimension
            new_width = int(max_dimension * aspect_ratio)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    return img

def create_html_for_folder(folder_path, script_location):
    folder_name = os.path.basename(folder_path)
    
    # Create the 'resized' folder within the current subfolder
    resized_folder = os.path.join(folder_path, 'resized')
    if not os.path.exists(resized_folder):
        os.makedirs(resized_folder)

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_files.sort(reverse=True)
    
    html_content = ''

    for image_file in image_files:
        rel_image_path = os.path.relpath(os.path.join(folder_path, image_file), script_location)
        img = resize_image(os.path.join(folder_path, image_file), 600)

        # Save the resized image to the 'resized' folder within the current subfolder
        resized_image_path = os.path.join(resized_folder, f'{folder_name}_{image_file}')
        img.save(resized_image_path)

        div_content = f'<div class="artImage">\n  <img src="{os.path.relpath(resized_image_path, script_location)}" alt="{image_file}" data="{rel_image_path}">\n</div>\n'
        html_content += div_content

    html_content += '<div class="artImage"></div>'

    output_file = os.path.join(script_location, 'art', f'{folder_name}_src.html')
    with open(output_file, 'w') as file:
        file.write(html_content)

    print(f'HTML file "{output_file}" created successfully.')

def create_html_for_all_subfolders(root_folder):
    script_location = os.path.dirname(os.path.abspath(__file__))
    root_folder_path = os.path.join(script_location, root_folder)

    for folder_name in os.listdir(root_folder_path):
        folder_path = os.path.join(root_folder_path, folder_name)

        if os.path.isdir(folder_path):
            create_html_for_folder(folder_path, script_location)

root_folder = 'art'
create_html_for_all_subfolders(root_folder)