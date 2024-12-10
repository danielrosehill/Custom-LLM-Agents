import os
import pandas as pd

# Function to find the root of the repository
def find_repo_root():
    current_dir = os.getcwd()
    while current_dir != '/':
        if '.git' in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    raise FileNotFoundError("Repository root not found")

# Function to update the README file
def update_readme():
    repo_root = find_repo_root()
    csv_path = os.path.join(repo_root, 'list.csv')
    readme_path = os.path.join(repo_root, 'README.md')

    # Read the CSV file
    if not os.path.exists(csv_path):
        raise FileNotFoundError("list.csv not found at the repository root")

    df = pd.read_csv(csv_path)

    # Convert the DataFrame to a Markdown table
    markdown_table = df.to_markdown(index=False)

    # Read the README file
    if not os.path.exists(readme_path):
        raise FileNotFoundError("README.md not found at the repository root")

    with open(readme_path, 'r') as file:
        readme_content = file.readlines()

    # Find the index of the '## Index' heading
    index_heading = '## Index\n'
    if index_heading not in readme_content:
        raise ValueError("'## Index' heading not found in README.md")

    index_position = readme_content.index(index_heading) + 1

    # Insert or update the Markdown table after the '## Index' heading
    updated_content = readme_content[:index_position] + [markdown_table + '\n'] + readme_content[index_position:]

    # Write the updated content back to the README file
    with open(readme_path, 'w') as file:
        file.writelines(updated_content)

# Simulate running the script from a subdirectory
if __name__ == "__main__":
    try:
        update_readme()
        print("README.md updated successfully.")
    except Exception as e:
        print(str(e))