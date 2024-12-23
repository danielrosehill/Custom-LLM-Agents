import os
from datetime import datetime

def find_repo_root():
    current_dir = os.getcwd()
    while current_dir != '/':
        if '.git' in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None

def get_last_run_time(md_path):
    if not os.path.exists(md_path):
        return None
    with open(md_path, 'r') as mdfile:
        lines = mdfile.readlines()
        if len(lines) > 1:
            for line in lines[2:]:
                if '|' in line:
                    date_str = line.split('|')[1].strip()
                    try:
                        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        continue
    return None

def find_new_markdown_files(repo_root, last_run_time, changelog_path):
    new_files = []
    changelog_rel_path = os.path.relpath(changelog_path, repo_root)
    
    for root, _, files in os.walk(repo_root):
        # Skip the non-docs directory
        if 'non-docs' in root.split(os.path.sep):
            continue
            
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, repo_root)
                
                if rel_path == changelog_rel_path:
                    continue
                    
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if not last_run_time or creation_time > last_run_time:
                    new_files.append((creation_time, file, rel_path))
    return sorted(new_files, key=lambda x: x[0], reverse=True)

def update_changelog(md_path, new_files):
    if not os.path.exists(md_path):
        content = "| Date | File Name | Path |\n|------|-----------|------|\n"
    else:
        with open(md_path, 'r') as mdfile:
            content = mdfile.read()
            if not content:
                content = "| Date | File Name | Path |\n|------|-----------|------|\n"
            elif "---" not in content:
                content = "| Date | File Name | Path |\n|------|-----------|------|\n" + content

    existing_entries = set()
    for line in content.splitlines():
        if '|' in line and 'Date' not in line and '---' not in line:
            if '[link](' in line:
                path = line.split('[link](')[1].split(')')[0]
                existing_entries.add(path)

    new_entries = ""
    for creation_time, file_name, rel_path in new_files:
        if rel_path not in existing_entries:
            new_entries += f"| {creation_time.strftime('%Y-%m-%d %H:%M:%S')} | {file_name} | [link]({rel_path}) |\n"
            existing_entries.add(rel_path)

    parts = content.split('\n', 2)
    if len(parts) >= 3:
        content = f"{parts[0]}\n{parts[1]}\n{new_entries}{parts[2]}"
    else:
        content = f"{parts[0]}\n{parts[1]}\n{new_entries}"

    with open(md_path, 'w') as mdfile:
        mdfile.write(content)

def main():
    repo_root = find_repo_root()
    if not repo_root:
        print("Git repository root not found. Please ensure the script is running inside a Git repository.")
        return

    changelog_path = os.path.join(repo_root, 'changelog.md')
    last_run_time = get_last_run_time(changelog_path)
    new_files = find_new_markdown_files(repo_root, last_run_time, changelog_path)
    update_changelog(changelog_path, new_files)

if __name__ == "__main__":
    main()
