import os
from datetime import datetime
import re

def find_repo_root():
    current_dir = os.getcwd()
    while current_dir != '/':
        if '.git' in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None

def find_new_markdown_files(repo_root, readme_path):
    new_files = []
    readme_rel_path = os.path.relpath(readme_path, repo_root)
    for root, _, files in os.walk(repo_root):
        if 'non-docs' in root.split(os.path.sep):
            continue
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, repo_root)
                if rel_path == readme_rel_path:
                    continue
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                badge = find_badge_in_file(file_path)
                assistant_name = ' '.join(word.capitalize() for word in file.replace('.md', '').split('-'))
                new_files.append((assistant_name, creation_time, file, rel_path, badge))
    return sorted(new_files, key=lambda x: x)  # Sort alphabetically by assistant_name (index 0)

def find_badge_in_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        match = re.search(r'\[!\[View on Hugging Face\]\(https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34\?style=for-the-badge&logo=huggingface&logoColor=white\)\]\(https://hf\.co/chat/assistant/[\w/]+\)', content)
        if match:
            return match.group(0)
    return ''

def update_readme(readme_path, new_files):
    with open(readme_path, 'r') as mdfile:
        content = mdfile.readlines()

    index_start = None
    index_end = None

    for i, line in enumerate(content):
        if line.strip() == "## Index":
            index_start = i + 1
        elif index_start is not None and line.startswith("## "):
            index_end = i
            break

    if index_start is None:
        print("## Index section not found in README.md")
        return

    if index_end is None:
        index_end = len(content)

    new_index_content = (
        "| Updated | Assistant Name | Repo Link | Use Now |\n"
        "|---------------|----------------|-----------|---------|\n"
    )

    total_assistants = len(new_files)
    total_hf_links = sum(1 for _, _, _, _, badge in new_files if badge)

    for assistant_name, creation_time, file_name, rel_path, badge in new_files:
        github_badge = f'[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)]({rel_path})'
        formatted_date = creation_time.strftime('%b %d (%Y)')
        new_index_content += f"| {formatted_date} | {assistant_name} | {github_badge} | {badge} |\n"

    # Add a blank line after the index
    new_index_content += "\n"

    # Add the totals section as a markdown table immediately after the index
    totals_section = (
        "## Total Count\n\n"
        "| Metric | Count |\n"
        "|-------------------------|-------|\n"
        f"| Total Assistants | {total_assistants} |\n"
        f"| Total on Hugging Face | {total_hf_links} |\n\n"
    )

    # Inject both the index and totals section into the README
    content = content[:index_start] + [new_index_content] + [totals_section] + content[index_end:]

    with open(readme_path, 'w') as mdfile:
        mdfile.writelines(content)

def main():
    repo_root = find_repo_root()
    if not repo_root:
        print("Git repository root not found. Please ensure the script is running inside a Git repository.")
        return

    readme_path = os.path.join(repo_root, 'README.md')
    if not os.path.exists(readme_path):
        print("README.md not found.")
        return

    new_files = find_new_markdown_files(repo_root, readme_path)
    update_readme(readme_path, new_files)

if __name__ == "__main__":
    main()
