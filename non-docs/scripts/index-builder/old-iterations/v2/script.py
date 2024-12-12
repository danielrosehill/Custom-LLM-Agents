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
                if not last_run_time or creation_time > last_run_time:
                    new_files.append((creation_time, file, rel_path))
    return sorted(new_files, key=lambda x: x[0], reverse=True)

def update_readme(readme_path, new_files):
    if not os.path.exists(readme_path):
        content = "# Repository Documentation\n\n## Index\n\n| Date | File Name | Path |\n|------|-----------|------|\n"
    else:
        with open(readme_path, 'r') as mdfile:
            content = mdfile.read()

    # Find the Index section
    index_match = re.search(r'(## Index\s*\n)', content)
    if not index_match:
        if content:
            content += "\n## Index\n\n| Date | File Name | Path |\n|------|-----------|------|\n"
        else:
            content = "# Repository Documentation\n\n## Index\n\n| Date | File Name | Path |\n|------|-----------|------|\n"
        index_pos = len(content)
        table_header_exists = False
    else:
        index_pos = index_match.end()
        # Check if table header exists
        table_header_exists = bool(re.search(r'\|\s*Date\s*\|\s*File Name\s*\|\s*Path\s*\|', content[index_pos:]))

    # Extract existing entries
    existing_entries = set()
    for line in content.splitlines():
        if '|' in line and '[link](' in line:
            path = line.split('[link](')[1].split(')')[0]
            existing_entries.add(path)

    # Prepare new entries
    new_content = ""
    if not table_header_exists:
        new_content = "| Date | File Name | Path |\n|------|-----------|------|\n"

    for creation_time, file_name, rel_path in new_files:
        if rel_path not in existing_entries:
            new_content += f"| {creation_time.strftime('%Y-%m-%d %H:%M:%S')} | {file_name} | [link]({rel_path}) |\n"
            existing_entries.add(rel_path)

    if new_content:
        # Insert new content after the index header and existing table header
        if table_header_exists:
            table_header_match = re.search(r'\|\s*Date\s*\|\s*File Name\s*\|\s*Path\s*\|\s*\n\|[-\s|]*\n', content[index_pos:])
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
    
    # Get existing content for last run time check
    existing_content = ""
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            existing_content = f.read()
    
    last_run_time = get_last_run_time(existing_content)
    new_files = find_new_markdown_files(repo_root, last_run_time, readme_path)
    update_readme(readme_path, new_files)

if __name__ == "__main__":
    main()
