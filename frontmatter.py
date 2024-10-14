import os
from glob import glob

# Path to the /Agents directory (adjust this if necessary)
agents_path = './Agents'

# Frontmatter template to be added to each .md file
frontmatter = '''---
creation_date:  
added_to_hugging_face:  
hugging_face_url:  
chatgpt_url:  
---
'''

# Recursively find all .md files under the /Agents directory
md_files = glob(os.path.join(agents_path, '**', '*.md'), recursive=True)

# Function to add frontmatter to .md files
def add_frontmatter_to_md(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        # Check if the file already has frontmatter
        if not content.startswith('---'):
            # Add frontmatter to the top of the file
            file.seek(0, 0)
            file.write(frontmatter + '\n' + content)

# Iterate through each .md file and add the frontmatter
for md_file in md_files:
    add_frontmatter_to_md(md_file)

print(f"Processed {len(md_files)} markdown files.")
