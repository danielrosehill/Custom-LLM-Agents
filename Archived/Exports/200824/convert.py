import pandas as pd

file_path = 'list.csv'  
df = pd.read_csv(file_path)


markdown_file = 'list.md'

with open(markdown_file, 'w') as file:
    for index, row in df.iterrows():
        file.write(f"## {row['Name']}\n")
        file.write(f"{row['Summary']}\n\n")
        file.write(f"[View On ChatGPT]({row['Link']})\n\n")
        file.write("---\n\n")

print(f"Markdown file '{markdown_file}' has been created.")
