import os
import csv

def format_title(file_name):
    """
    Convert snake_case or kebab-case file name to readable text.
    Replace '-' with spaces and ensure all text is lowercase.
    """
    return file_name.replace('-', ' ').lower()

def generate_csv():
    """
    Generate a four-column CSV file at the root of the repository with readable titles,
    relative paths, and additional columns for HuggingFace status and URL. Avoid duplicate
    entries when the script is run repeatedly.
    """
    # Get the absolute path of the current working directory
    current_dir = os.path.abspath(os.getcwd())

    # Find the base directory of the repository
    while not os.path.exists(os.path.join(current_dir, '.git')):  # Assuming a .git folder marks the repo root
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached root without finding .git
            raise RuntimeError("Could not find the base of the repository.")
        current_dir = parent_dir

    base_dir = current_dir  # The root of the repository

    # Initialize a list to store markdown file names and their relative paths
    markdown_files = []

    # Walk through the directory tree starting from the base directory
    for root, dirs, files in os.walk(base_dir):
        # Skip the 'non-docs' directory
        if 'non-docs' in dirs:
            dirs.remove('non-docs')
        if root == base_dir and 'README.md' in files:
            files.remove('README.md')
        for file in files:
            if file.endswith('.md'):
                # Get relative path and file name without extension
                relative_path = os.path.relpath(os.path.join(root, file), base_dir)
                markdown_files.append((file[:-3], relative_path))

    # Define the path for the CSV file at the base of the repository
    csv_path = os.path.join(base_dir, 'list.csv')
    memory_path = os.path.join(base_dir, '.processed_files.txt')

    # Read existing entries from the CSV if it exists
    existing_titles = set()
    if os.path.exists(csv_path):
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # Skip header row
            for row in reader:
                if row:  # Add only non-empty rows
                    existing_titles.add(row[0])  # Add title (first column) to set

    # Read processed files from memory if it exists
    processed_files = set()
    if os.path.exists(memory_path):
        with open(memory_path, mode='r', encoding='utf-8') as memory_file:
            for line in memory_file:
                processed_files.add(line.strip())

    # Prepare a list to store new entries
    new_entries = []

    # Process markdown files
    for file_name, relative_path in markdown_files:
        formatted_title = format_title(file_name)
        if formatted_title not in existing_titles and relative_path not in processed_files:
            new_entries.append((formatted_title, relative_path))
            processed_files.add(relative_path)

    # Sort new entries by title
    new_entries.sort(key=lambda x: x[0])

    # Write markdown file names to CSV with formatting, avoiding duplicates
    with open(csv_path, mode='a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        if not os.path.exists(csv_path) or os.stat(csv_path).st_size == 0:  # Write header row only if new file
            writer.writerow(['title', 'relative_path', 'added_to_huggingface', 'huggingfacechaturl'])
        for formatted_title, relative_path in new_entries:
            writer.writerow([formatted_title, relative_path, '', ''])  # Empty values for added_to_huggingface and huggingfacechaturl

    # Write processed files to memory
    with open(memory_path, mode='w', encoding='utf-8') as memory_file:
        for relative_path in processed_files:
            memory_file.write(f"{relative_path}\n")

# Call the function to generate CSV
generate_csv()