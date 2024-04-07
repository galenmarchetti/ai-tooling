import tiktoken
import os
import argparse

MODEL_NAME="gpt-4-0125-preview"
CONTEXT_WINDOW=128000

def get_tokens_in_text(text):
    encoded = encoding = tiktoken.encoding_for_model(MODEL_NAME)
    num_tokens = len(encoding.encode(text))
    return num_tokens

# Function to count tokens in a single file
def count_tokens_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        encoding = tiktoken.encoding_for_model(MODEL_NAME)
        num_tokens = len(encoding.encode(content))
        return num_tokens
    except Exception as e:
        print(f"\tError processing file {file_path}: {e}")
        return 0

# Function to recursively count tokens in a directory
def count_tokens_in_directory(directory_path):
    token_count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            token_count += count_tokens_in_file(file_path)
    return token_count

def main():
    parser = argparse.ArgumentParser(description='Token count for files and directories.')
    parser.add_argument('paths', nargs='+', help='Paths to files and/or directories')
    parser.add_argument('-d', '--directories-only', action='store_true', help='Operate on directories only')
    parser.add_argument('-f', '--files-only', action='store_true', help='Operate on files only')
    
    args = parser.parse_args()

    for path in args.paths:
        if args.directories_only:
            if os.path.isdir(path):
                print(f"{path}: {count_tokens_in_directory(path)} tokens")
        elif args.files_only:
            if os.path.isfile(path):
                print(f"{path}: {count_tokens_in_file(path)} tokens")
        elif not os.path.exists(path):
            print(f"{path}: Path does not exist")
        else:
            if os.path.isfile(path):
                print(f"\t{path}: {count_tokens_in_file(path)} tokens")
            elif os.path.isdir(path):
                print(f"{path}: {count_tokens_in_directory(path)} tokens")

if __name__ == "__main__":
    main()