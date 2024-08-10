import os
import subprocess

relative_directory = 'GPTs'
output_file = 'folder_structure.md'

def generate_folder_structure_markdown():
    directory = os.path.abspath(relative_directory)
    if os.path.isdir(directory):
        result = subprocess.run(['tree', '-d', directory], stdout=subprocess.PIPE, text=True)
        tree_output = result.stdout
        markdown_output = "```\n" + tree_output + "\n```"
        with open(output_file, 'w') as f:
            f.write(markdown_output)
        print(f"Folder structure markdown saved to {output_file}")
    else:
        print(f"Error: Directory {directory} does not exist or cannot be accessed.")

generate_folder_structure_markdown()
