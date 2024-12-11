import os
import csv
from datetime import datetime

def find_repo_root():
    """Recursively find the root of the GitHub repository."""
    current_dir = os.getcwd()
    while current_dir != '/':
        if '.git' in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None

def get_last_run_time(csv_path):
    """Retrieve the last run time from the changelog CSV."""
    if not os.path.exists(csv_path):
        return None
    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            return datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
    return None

def find_new_markdown_files(repo_root, last_run_time):
    """Find new markdown files created since the last run."""
    new_files = []
    for root, _, files in os.walk(repo_root):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if not last_run_time or creation_time > last_run_time:
                    new_files.append((creation_time, file, os.path.relpath(file_path, repo_root)))
    return sorted(new_files, key=lambda x: x[0], reverse=True)

def update_changelog(csv_path, new_files):
    """Update the changelog CSV with new markdown files."""
    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for creation_time, file_name, rel_path in new_files:
            writer.writerow([creation_time.strftime('%Y-%m-%d %H:%M:%S'), file_name, rel_path])

def main():
    repo_root = find_repo_root()
    if not repo_root:
        print("Git repository root not found. Please ensure the script is running inside a Git repository.")
        return

    changelog_path = os.path.join(repo_root, 'changelog.csv')
    last_run_time = get_last_run_time(changelog_path)
    new_files = find_new_markdown_files(repo_root, last_run_time)

    if not os.path.exists(changelog_path):
        with open(changelog_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'File Name', 'Path'])

    update_changelog(changelog_path, new_files)

if __name__ == "__main__":
    main()
