import subprocess
import os
import sys

def get_git_root():
    """Return the root directory of the git repository."""
    try:
        # git rev-parse --show-toplevel returns the absolute path of the top-level directory
        return subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        print("Error: Unable to find the git repository root.")
        sys.exit(1)

def is_git_ignored(file_path):
    """Check if the file is ignored by git."""
    try:
        subprocess.check_call(['git', 'check-ignore', '-q', file_path])
        return True
    except subprocess.CalledProcessError:
        return False

def concatenate_files(files, git_root):
    """Concatenate the contents of files, skipping binary or non-UTF-8 files and those ignored by git."""
    concatenated_contents = ""
    for file in files:
        # Convert the file path to be relative to the git root
        relative_path = os.path.relpath(file, git_root)
        if is_git_ignored(relative_path):
            print(f"Skipping git-ignored file: {relative_path}")
            continue
        if os.path.isfile(file):  # Check if it's a file and not a directory
            try:
                with open(file, 'r', encoding='utf-8') as file_handle:
                    contents = file_handle.read()
                    concatenated_contents += f"{relative_path}:\n\n{contents}\n\n---\n\n"
            except UnicodeDecodeError:
                print(f"Warning: Skipping binary or non-UTF-8 file {relative_path}")
    return concatenated_contents

def main(files):
    git_root = get_git_root()
    concatenated_contents = concatenate_files(files, git_root)
    
    # Print or save concatenated_contents as needed
    print(concatenated_contents)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file1> <file2> ...")
    else:
        main(sys.argv[1:])

