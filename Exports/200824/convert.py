import pandas as pd
file_path = 'GPTList.csv'
df = pd.read_csv(file_path)

markdown_file = 'list.md'

with open(markdown_file, 'w') as file:
    for index, row in df.iterrows():
        file.write(f"## {row['Name']}\n")
        file.write(f"{row['Summary']}\n\n")
        file.write(f"[View GPT]({row['Link']})\n\n")

print(f"Markdown file '{markdown_file}' has been created.")
