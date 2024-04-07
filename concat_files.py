import sys
import os

def concatenate_files(filepaths):
    result = ""
    for filepath in filepaths:
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                result += f"{filepath}:\n\n"
                result += f"{f.read()}\n\n---\n"
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepaths = sys.argv[1:]
        print(concatenate_files(filepaths))
    else:
        print("Please provide one or more file paths as command-line arguments.")
