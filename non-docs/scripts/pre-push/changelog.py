import os
from datetime import datetime

# Function to get word count of a file
def get_word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return len(content.split())

# Function to scan repository and update changelog
def update_changelog(repo_path, changelog_name='changelog.md', exclude_dir='non-docs'):
    # Get absolute paths
    repo_path = os.path.abspath(repo_path)
    changelog_path = os.path.join(repo_path, changelog_name)
    
    # Read existing changelog entries
    if os.path.exists(changelog_path):
        with open(changelog_path, 'r', encoding='utf-8') as changelog_file:
            existing_entries = changelog_file.read()
    else:
        existing_entries = ''

    # Traverse the repository
    new_entries = []
    for root, dirs, files in os.walk(repo_path):
        # Skip the exclude directory
        if exclude_dir in os.path.relpath(root, repo_path).split(os.sep):
            continue
        
        for file in files:
            if file.endswith('.md') and file != changelog_name:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, repo_path)
                file_name = os.path.splitext(file)[0]  # Remove .md extension
                
                # Check if the file is already recorded
                if f"## {file_name}" not in existing_entries:
                    word_count = get_word_count(file_path)
                    timestamp = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    entry = (
                        f"## {file_name}\n"
                        f"[{file_name}]({relative_path})\n"
                        f"Word Count: {word_count}\n"
                        f"Created: {timestamp}\n"
                    )
                    new_entries.append(entry)

    # Update the changelog if there are new entries
    if new_entries:
        with open(changelog_path, 'w', encoding='utf-8') as changelog_file:
            changelog_file.write('\n'.join(new_entries) + '\n' + existing_entries)

# Example usage
# Replace '/path/to/repo' with the actual path to your repository
update_changelog('/path/to/repo')
