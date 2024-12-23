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

def get_last_run_time(content):
    if not content:
        return None
    matches = re.findall(r'\|\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s*\|', content)
    if matches:
        try:
            return max(datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S') for date_str in matches)
        except ValueError:
            return None
    return None

def find_new_markdown_files(repo_root, last_run_time, readme_path):
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
                if not last_run_time or modification_time > last_run_time:
                    new_files.append((creation_time, file, rel_path, badge))
    return sorted(new_files, key=lambda x: x[0], reverse=True)

def find_badge_in_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        match = re.search(r'\[!\[View on Hugging Face\]\(https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34\?style=for-the-badge&logo=huggingface&logoColor=white\)\]\(https://hf\.co/chat/assistant/[\w/]+\)', content)
        if match:
            return match.group(0)
    return ''

def update_readme(readme_path, new_files):
    if not os.path.exists(readme_path):
        content = "# Repository Documentation\n\n## Index\n\n| Date | Assistant Name | Repo Link | Hugging Face Badge |\n|------|----------------|-----------|------------------|\n"
    else:
        with open(readme_path, 'r') as mdfile:
            content = mdfile.read()

    index_match = re.search(r'(## Index\s*\n)', content)
    if not index_match:
        if content:
            content += "\n## Index\n\n| Date | Assistant Name | Repo Link | Hugging Face Badge |\n|------|----------------|-----------|------------------|\n"
        else:
            content = "# Repository Documentation\n\n## Index\n\n| Date | Assistant Name | Repo Link | Hugging Face Badge |\n|------|----------------|-----------|------------------|\n"
        index_pos = len(content)
        table_header_exists = False
    else:
        index_pos = index_match.end()
        table_header_exists = bool(re.search(r'\|\s*Date\s*\|\s*Assistant Name\s*\|\s*Repo Link\s*\|\s*Hugging Face Badge\s*\|', content[index_pos:]))

    existing_entries = {}
    for line in content.splitlines():
        if '|' in line and '[link](' in line:
            parts = line.split('|')
            path = parts[3].strip().split('[link](')[1].split(')')[0]
            badge = parts[4].strip()
            existing_entries[path] = badge

    new_content = ""
    if not table_header_exists:
        new_content = "| Date | Assistant Name | Repo Link | Hugging Face Badge |\n|------|----------------|-----------|------------------|\n"

    for creation_time, file_name, rel_path, badge in new_files:
        assistant_name = ' '.join(word.capitalize() for word in file_name.replace('.md', '').split('-'))
        github_badge = f'[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)]({rel_path})'
        if rel_path not in existing_entries:
            new_content += f"| {creation_time.strftime('%Y-%m-%d %H:%M:%S')} | {assistant_name} | {github_badge} | {badge} |\n"
        elif existing_entries[rel_path] != badge:
            new_content += f"| {creation_time.strftime('%Y-%m-%d %H:%M:%S')} | {assistant_name} | {github_badge} | {badge} |\n"
            # Replace the existing line with the new one
            content = re.sub(rf'\|\s*{re.escape(creation_time.strftime("%Y-%m-%d %H:%M:%S"))}\s*\|\s*{re.escape(assistant_name)}\s*\|\s*{re.escape(github_badge)}\s*\|\s*.*?\s*\|', 
                             f"| {creation_time.strftime('%Y-%m-%d %H:%M:%S')} | {assistant_name} | {github_badge} | {badge} |", content)

    if new_content:
        if table_header_exists:
            table_header_match = re.search(r'\|\s*Date\s*\|\s*Assistant Name\s*\|\s*Repo Link\s*\|\s*Hugging Face Badge\s*\|\s*\n\|[-\s|]*\n', content[index_pos:])
            if table_header_match:
                insert_pos = index_pos + table_header_match.end()
                content = content[:insert_pos] + new_content + content[insert_pos:]
        else:
            content = content[:index_pos] + "\n" + new_content + content[index_pos:]

    with open(readme_path, 'w') as mdfile:
        mdfile.write(content)

def main():
    repo_root = find_repo_root()
    if not repo_root:
        print("Git repository root not found. Please ensure the script is running inside a Git repository.")
        return

    readme_path = os.path.join(repo_root, 'README.md')
    
    existing_content = ""
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            existing_content = f.read()
    
    last_run_time = get_last_run_time(existing_content)
    new_files = find_new_markdown_files(repo_root, last_run_time, readme_path)
    update_readme(readme_path, new_files)

if __name__ == "__main__":
    main()