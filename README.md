# AI Tooling

Some scripts to help people use chat-based LLMs, especially for coding help.

##Installation

Just run 

```bash
pip install -r requirements.txt
``` 

in the root of this repository to install the python requirements for these scripts.

## Usage

### Concat Files

```bash
python concat_files.py <LIST_OF_FILES>
``` 

will concatenate the relative paths and the contents of the files passed in. I use it like this:


```bash
python concat_files **/** | pbcopy
``` 

so I can then paste the directory structure and the contents of the files into a chat interface.

### Concat Git Files

```bash
python concat_git_files.py <LIST_OF_FILES>
``` 

is used for files in a git directory, when you want to make sure you ignore all the files that are ignored by `.gitignore`. This behaves the same way as `concat_files` except for the caveat that you need to run it within a git directory. I use it like this:


```bash
python concat_git_files **/** | pbcopy
``` 

so I can then paste the directory structure and the contents of the files of a git repo into a chat interface, automatically ignoring things like build artifacts or sensitive information that is usually ignored by `.gitignore`.

### Tokens In Input

```bash
python tokens_in_input.py <LIST_OF_FILES_AND_DIRECTORIES>
``` 

is used for counting how many tokens are in the input files. It also sums the number of tokens within all the files of a directory, and displays that next to the directory path, if the input is a directory. It uses `tiktoken` and you have to change the constants `MODEL_NAME` and `CONTEXT_WINDOW` manually in order to specify the model that you want to tokenize for (i.e. `chat-gpt4-0125-preview` has a context window of `128000` tokens according to OpenAI's documentation.) Refer to `tiktoken` for available models and OpenAI's docs for the context window lengths. The context window length is really only for display purposes so you can see as you read the output how much space you have per prompt.

### Prompt

`prompt.py` is something I'm just playing with, not sure what I'm going to do with that yet.