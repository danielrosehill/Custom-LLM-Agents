import os
import yaml

def find_markdown_files_with_status(repo_root, status_key, status_value):
    """
    Find all markdown files in the repository with the specified status in their front matter.
    """
    matching_files = []
    for root, _, files in os.walk(repo_root):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if content.startswith('---'):
                            metadata = yaml.safe_load(content.split('---')[1])
                            if metadata.get(status_key) == status_value:
                                matching_files.append(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return matching_files

def generate_markdown_table(files, repo_root):
    """
    Generate a markdown table from the list of files.
    """
    table = "| Title | Link |\n|-------|------|\n"
    for file in sorted(files):
        title = os.path.splitext(os.path.basename(file))[0]  # Remove .md extension
        relative_path = os.path.relpath(file, repo_root)  # Relative path from repo root
        link = f"[link]({relative_path})"
        table += f"| {title} | {link} |\n"
    return table

def main():
    # Determine the repository root by walking up until a .git folder is found
    current_dir = os.getcwd()
    while not os.path.exists(os.path.join(current_dir, ".git")):
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached the filesystem root
            raise RuntimeError("Repository root not found. Ensure this script is inside a Git repository.")
        current_dir = parent_dir

    repo_root = current_dir
    status_key = "hf_status"
    status_value = "Pending"
    
    # Find markdown files with the specified status
    matching_files = find_markdown_files_with_status(repo_root, status_key, status_value)
    
    # Generate a markdown header and description
    header = (
        "# Hugging Face Addition Queue\n\n"
        "This Markdown file lists a queue of configured agents which are going to be added as assistants on Hugging Face in the near future. "
        "Once they have been added, their URLs are noted in this repository so that anyone can use them.\n\n"
    )
    
    # Generate a markdown table
    markdown_table = generate_markdown_table(matching_files, repo_root)
    
    # Combine header and table
    output_content = header + markdown_table
    
    # Write the content to a markdown file
    output_file = os.path.join(repo_root, "pending_files.md")
    with open(output_file, "w") as f:
        f.write(output_content)
    
    print(f"Markdown table written to {output_file}")

if __name__ == "__main__":
    main()