import os
import shutil

def move_files_to_folders(root_folder):
    # Recursively iterate through all files and folders in the root folder
    for root, dirs, files in os.walk(root_folder):
        for txt_file in files:
            if txt_file.endswith(".txt"):
                txt_file_path = os.path.join(root, txt_file)

                # Read the list of file paths from the txt file
                with open(txt_file_path, 'r') as file:
                    file_paths = file.read().splitlines()

                # Move each file to the folder containing the txt file
                for file_path in file_paths:
                    # Remove the string "r/" from the file path
                    file_path = file_path.replace("r/", "")

                    file_name = os.path.basename(file_path)
                    parent_folder = os.path.dirname(file_path)
                    og_folder = os.path.join(parent_folder, 'og')

                    # Create the 'og' subfolder if it doesn't exist
                    if not os.path.exists(og_folder):
                        os.makedirs(og_folder)

                    # Move the file to the 'og' subfolder
                    destination_path = os.path.join(og_folder, file_name)
                    shutil.move(file_path, destination_path)
                    print(f"Moved {file_name} to {og_folder}")

if __name__ == "__main__":
    # Replace 'your_root_folder' with the path to the folder containing your subfolders
    move_files_to_folders('sketchbooks')