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
    Generate a two-column CSV file at the base of the repository with readable titles
    and HuggingFace identifiers derived from markdown file names in the repository.
    Avoid duplicate entries when the script is run repeatedly.
    """
    # Get the absolute path of the current working directory
    current_dir = os.path.abspath(os.getcwd())

    # Find the base directory of the repository
    while not os.path.exists(os.path.join(current_dir, '.git')):  # Assuming a .git folder marks the repo root
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached root without finding .git
            raise RuntimeError("Could not find the base of the repository.")
        current_dir = parent_dir

    base_dir = current_dir

    # Initialize a list to store markdown file names
    markdown_files = []

    # Walk through the directory tree starting from where the script is executed
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.md'):
                # Append the file name without extension
                markdown_files.append(file[:-3])

    # Define the path for the CSV file at the base of the repository
    csv_path = os.path.join(base_dir, 'list.csv')

    # Read existing entries from the CSV if it exists
    existing_titles = set()
    if os.path.exists(csv_path):
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # Skip header row
            for row in reader:
                if row:  # Add only non-empty rows
                    existing_titles.add(row[0])  # Add title (first column) to set

    # Write markdown file names to CSV with formatting, avoiding duplicates
    with open(csv_path, mode='a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        if not os.path.exists(csv_path) or os.stat(csv_path).st_size == 0:  # Write header row only if new file
            writer.writerow(['Title', 'HuggingFace'])
        for file_name in markdown_files:
            formatted_title = format_title(file_name)
            if formatted_title not in existing_titles:
                writer.writerow([formatted_title, 'Added to HuggingFace'])

# Call the function to generate CSV
generate_csv()