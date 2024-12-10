import os
import csv

def find_repo_root():
    """Finds the root directory of the repository by looking for .git folder."""
    current_dir = os.getcwd()
    while current_dir != '/':
        if '.git' in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None

def read_csv(file_path):
    """Reads the CSV file and returns its content as a list of dictionaries."""
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def generate_markdown_table(data):
    """Generates a markdown table from CSV data."""
    if not data:
        return ""
    
    # Define headers for the table
    headers = ["Title", "HuggingFace URL", "Repository File Link"]
    table = f"| {' | '.join(headers)} |\n"
    table += f"| {' | '.join(['---'] * len(headers))} |\n"
    
    for row in data:
        title = row.get("title", "")
        huggingface_url = row.get("huggingfacechaturl", "")
        relative_path = row.get("relative_path", "")
        
        # Create links for HuggingFace URL and Repository File Link
        huggingface_link = f"[link]({huggingface_url})" if huggingface_url else ""
        repo_file_link = f"[link]({relative_path})" if relative_path else ""
        
        # Add a row to the table
        table += f"| {title} | {huggingface_link} | {repo_file_link} |\n"
    
    return table

def inject_into_readme(readme_path, table_content):
    """Injects the markdown table into README.md under ## Index."""
    with open(readme_path, 'r') as file:
        lines = file.readlines()
    
    # Check if the table already exists
    start_marker = "<!-- START OF GENERATED TABLE -->"
    end_marker = "<!-- END OF GENERATED TABLE -->"
    
    start_index = None
    end_index = None
    
    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        if end_marker in line:
            end_index = i
    
    # If table exists, replace it
    if start_index is not None and end_index is not None:
        del lines[start_index:end_index + 1]
    
    # Find where to insert the table (after ## Index)
    index_header = "## Index"
    for i, line in enumerate(lines):
        if line.strip() == index_header:
            insertion_point = i + 1
            break
    else:
        raise ValueError("## Index header not found in README.md")
    
    # Insert new table with markers
    new_table_section = f"{start_marker}\n{table_content}{end_marker}\n"
    lines.insert(insertion_point, new_table_section)
    
    # Write back to README.md
    with open(readme_path, 'w') as file:
        file.writelines(lines)

def main():
    repo_root = find_repo_root()
    
    if not repo_root:
        print("Repository root not found.")
        return
    
    list_csv_path = os.path.join(repo_root, 'list.csv')
    readme_path = os.path.join(repo_root, 'README.md')
    
    if not os.path.exists(list_csv_path):
        print("list.csv not found in the repository root.")
        return
    
    if not os.path.exists(readme_path):
        print("README.md not found in the repository root.")
        return
    
    csv_data = read_csv(list_csv_path)
    
    if not csv_data:
        print("list.csv is empty or invalid.")
        return
    
    markdown_table = generate_markdown_table(csv_data)
    
    inject_into_readme(readme_path, markdown_table)
    
    print("Table injected successfully into README.md.")

if __name__ == "__main__":
    main()