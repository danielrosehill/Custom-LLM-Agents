import os
import re
import json

def find_markdown_files(base_path, exclude_dirs, exclude_files):
    """Recursively find all markdown files in the repository, excluding specified directories and files."""
    markdown_files = []
    for root, dirs, files in os.walk(base_path):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if os.path.relpath(os.path.join(root, d), base_path) not in exclude_dirs]
        
        for file in files:
            if file.endswith('.md') and file not in exclude_files:
                relative_path = os.path.relpath(os.path.join(root, file), base_path)
                markdown_files.append(relative_path)
    return markdown_files

def format_title(file_name):
    """Convert a file name to readable case with proper capitalization."""
    name_without_extension = os.path.splitext(file_name)[0]
    # Replace hyphens with spaces and capitalize each word
    readable_name = re.sub(r'[-_]', ' ', name_without_extension).title()
    return readable_name

def create_markdown_table(markdown_files):
    """Create a markdown table for the list of markdown files."""
    # Sort files alphabetically by their formatted title
    sorted_files = sorted(markdown_files, key=lambda f: format_title(os.path.basename(f)))
    
    table_lines = ['| Title | Link |', '|-------|------|']
    for file in sorted_files:
        file_name = os.path.basename(file)
        title = format_title(file_name)
        table_lines.append(f'| {title} | [link]({file}) |')  # Removed './' from the link
    return '\n'.join(table_lines)

def insert_into_readme(readme_path, table):
    """Insert the markdown table into README.md under '## Index'."""
    with open(readme_path, 'r') as f:
        content = f.read()

    index_heading = '## Index'
    if index_heading in content:
        parts = content.split(index_heading)
        before_index = parts[0] + index_heading + '\n\n'
        after_index = '\n'.join(parts[1].split('\n')[1:])  # Skip existing table
        new_content = before_index + table + '\n' + after_index
    else:
        new_content = content + '\n\n' + index_heading + '\n\n' + table

    with open(readme_path, 'w') as f:
        f.write(new_content)

def save_memory(memory_path, markdown_files):
    """Save the list of markdown files to a memory file."""
    with open(memory_path, 'w') as f:
        json.dump(markdown_files, f)

def load_memory(memory_path):
    """Load the list of markdown files from the memory file."""
    if os.path.exists(memory_path):
        with open(memory_path, 'r') as f:
            return json.load(f)
    return []

def update_memory(memory_path, new_files):
    """Update the memory file with new markdown files."""
    existing_files = load_memory(memory_path)
    updated_files = sorted(set(existing_files + new_files))
    save_memory(memory_path, updated_files)
    return updated_files

# Main script execution
if __name__ == "__main__":
    base_path = '.'
    readme_path = 'README.md'
    
    # Ensure memory file is stored in the same directory as this script
    memory_path = os.path.join(os.path.dirname(__file__), 'file_memory.json')
    
    # Directories and files to exclude
    exclude_dirs = ['non-docs']
    exclude_files = ['README.md']

    # Find all markdown files excluding specified directories and files
    markdown_files = find_markdown_files(base_path, exclude_dirs, exclude_files)

    # Update memory to avoid duplicates
    updated_files = update_memory(memory_path, markdown_files)

    # Create a markdown table
    markdown_table = create_markdown_table(updated_files)

    # Insert the table into README.md
    insert_into_readme(readme_path, markdown_table)