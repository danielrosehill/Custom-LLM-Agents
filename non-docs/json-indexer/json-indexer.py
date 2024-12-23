import os
import re
import json

def find_repo_base(start_path):
    """
    Dynamically finds the base of the repository by looking for a `.git` folder.
    If not found, defaults to the provided start_path.
    """
    current_path = start_path
    while current_path != os.path.dirname(current_path):  # Stop at root directory
        if ".git" in os.listdir(current_path):
            return current_path
        current_path = os.path.dirname(current_path)
    return start_path  # Default to start_path if .git is not found

def extract_hf_url(content):
    """
    Extracts the Hugging Face URL from the markdown content.
    Updated regex to exclude closing parentheses `)`.
    """
    match = re.search(r'https://hf\.co/chat/assistant[^\s\)]*', content)
    return match.group(0) if match else None

def create_assistant_index(repo_base, exclude_folder, output_file):
    """
    Creates a JSON index of assistants based on Markdown files in a repository.
    
    Parameters:
        repo_base (str): The base path of the repository.
        exclude_folder (str): Folder to exclude from processing.
        output_file (str): Path to save the generated JSON file.
    """
    assistants = []

    for root, dirs, files in os.walk(repo_base):
        # Skip the excluded folder
        if exclude_folder in root:
            continue

        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)

                # Exclude markdown files at the base of the repository
                if root == repo_base and file.lower() == "readme.md":
                    continue
                if root == repo_base:
                    continue

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract assistant title (file name without extension)
                title = os.path.splitext(file)[0]
                # Extract Hugging Face URL
                url = extract_hf_url(content)

                if url:
                    assistants.append({"title": title, "url": url})

    # Sort assistants alphabetically by title
    assistants.sort(key=lambda x: x["title"].lower())

    # Write to JSON file at the root of the repository
    output_file_path = os.path.join(repo_base, output_file)
    
    # Check if the file already exists and remove it to avoid duplicates
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(assistants, f, indent=4)

# Main logic
if __name__ == "__main__":
    current_directory = os.getcwd()  # Current working directory where script is run
    repo_base = find_repo_base(current_directory)  # Dynamically find repo base
    exclude_folder_name = "non-docs"  # Folder to exclude
    output_json_file = "assistants_index.json"  # Output JSON file name

    create_assistant_index(repo_base, exclude_folder_name, output_json_file)
