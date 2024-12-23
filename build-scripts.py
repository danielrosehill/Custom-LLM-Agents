import os
import subprocess

# Define the directory containing the Python scripts
scripts_directory = "/home/daniel/Git/Custom-LLM-Agents/non-docs/scripts/batches/231324/jobs"

def execute_scripts(directory):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Filter for Python scripts only
        python_scripts = [file for file in files if file.endswith(".py")]
        
        # Sort scripts to ensure sequential execution order (optional, based on naming)
        python_scripts.sort()
        
        # Execute each script sequentially
        for script in python_scripts:
            script_path = os.path.join(directory, script)
            print(f"Executing: {script_path}")
            
            # Run the Python script using subprocess
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)
            
            # Print the output and errors (if any)
            print("Output:")
            print(result.stdout)
            if result.stderr:
                print("Errors:")
                print(result.stderr)
            
            # Check if the script execution failed
            if result.returncode != 0:
                print(f"Script {script} failed with return code {result.returncode}")
                break  # Stop execution if a script fails
                
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the scripts in the specified directory
execute_scripts(scripts_directory)
