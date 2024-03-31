import tiktoken
import openai
import os
import sys

MODEL_NAME="gpt-3.5-turbo"
CONTEXT_WINDOW=16385

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
        print(f"Error processing file {file_path}: {e}")
        return 0

# Function to recursively count tokens in a directory
def count_tokens_in_directory(directory_path):
    token_count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            token_count += count_tokens_in_file(file_path)
    return token_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path1> <path2> ...")
        sys.exit(1)

    print(f"Context window for {MODEL_NAME} is {CONTEXT_WINDOW}\n")
    paths = sys.argv[1:]
    for path in paths:
        if os.path.isfile(path):
            print(f"\t- {path}: {count_tokens_in_file(path)} tokens")
        elif os.path.isdir(path):
            print(f"{path}: {count_tokens_in_directory(path)} tokens")
        else:
            print(f"{path}: Path does not exist")