import os
from glob import glob

# Path to the /Agents directory (adjust this if necessary)
agents_path = './Agents'

# The string pattern to be removed (the start of ## Link and URL)
pattern_to_remove = "## Link\nhttps://chatgpt.com/g/"

# Recursively find all .md files under the /Agents directory
md_files = glob(os.path.join(agents_path, '**', '*.md'), recursive=True)

# Function to remove the specific pattern from .md files
def remove_pattern_from_md(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        # Remove the entire section after ## Link and URL
        if pattern_to_remove in content:
            # Remove from "## Link" onwards
            modified_content = content.split(pattern_to_remove)[0]
            file.seek(0)
            file.write(modified_content)
            file.truncate()

# Iterate through each .md file and remove the pattern
for md_file in md_files:
    remove_pattern_from_md(md_file)

print(f"Processed {len(md_files)} markdown files.")
