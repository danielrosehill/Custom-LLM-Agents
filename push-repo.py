import os
import subprocess

# Directory containing the Python scripts
directory = '/home/daniel/Git/Custom-LLM-Agents/non-docs/scripts/batches/231324/jobs'

# Function to run all Python scripts in the directory
def run_python_scripts(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith('.py'):
                filepath = os.path.join(directory, filename)
                print(f"Running {filepath}...")
                result = subprocess.run(['python', filepath], capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"Error running {filepath}: {result.stderr}")
    else:
        print(f"Directory {directory} does not exist.")
        return False
    return True

# Function to perform git operations
def git_operations():
    try:
        # Stage changes
        subprocess.run(['git', 'add', '.'], check=True)
        print("Staged changes.")
        
        # Commit changes
        subprocess.run(['git', 'commit', '-m', 'updates'], check=True)
        print("Committed changes with message 'updates'.")
        
        # Push changes
        subprocess.run(['git', 'push'], check=True)
        print("Pushed changes to remote repository.")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")

# Main execution flow
if run_python_scripts(directory):
    git_operations()
