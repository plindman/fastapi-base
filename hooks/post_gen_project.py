import os
import subprocess
from pathlib import Path

def git_init():
    """Initialize a Git repository if the user opted for it."""
    git_init_choice = "{{ cookiecutter.git_init }}".strip().lower()
    
    if git_init_choice == "yes":
        if not (Path(".git").exists()):
            print("Initializing Git repository...")
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Initial commit from template"], check=True)
            print("Git repository initialized successfully.")
        else:
            print("Git repository already exists. Skipping git init.")

if __name__ == "__main__":
    git_init()
