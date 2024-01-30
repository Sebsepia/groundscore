import os

def create_html_files(root_folder):
    # Iterate through all subfolders in the root folder
    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)

        # Check if the subfolder has a 'cover' folder
        cover_folder = os.path.join(subfolder_path, 'cover')
        if os.path.exists(cover_folder):
            # Open a separate HTML file for each subfolder
            output_file = f'{subfolder}.html'
            with open(output_file, 'w') as html_file:

                # Write the sketchbook cover div and image
                html_file.write(f'<div class="sketchbook">\n<div class="sketchbook_cover">')
                cover_image_path = os.path.join(cover_folder, os.listdir(cover_folder)[0])
                html_file.write(f'<img src="{cover_image_path}" alt="Cover Image">\n</div>')

                # Write sketchbook pages inside the sketchbook_cover div
                for image_file in os.listdir(subfolder_path):
                    if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')) and image_file != 'cover':
                        image_path = os.path.join(subfolder_path, image_file)
                        html_file.write(f'<div class="sketchbook_page">\n')
                        html_file.write(f'<img src="{image_path}" alt="Page Image">\n')
                        html_file.write('</div>\n')

                # Close the sketchbook_cover div
                html_file.write('</div>\n')

if __name__ == "__main__":
    # Replace 'your_root_folder' with the path to the folder containing your subfolders
    create_html_files('sketchbooks')

    