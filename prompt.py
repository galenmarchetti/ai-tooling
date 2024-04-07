import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

# This function will load the environment variables from the .env file
load_dotenv()

MODEL_NAME = "gpt-4-0125-preview"

def get_api_key(env_var_name):
    """Get the OpenAI API key from environment variables."""
    return os.getenv(env_var_name)

async def send_prompt(client, prompt):
    """Send a prompt to OpenAI using the provided API key."""
    message = {
        "role": "user",
        "content": prompt
    }
    stream = await client.chat.completions.create(
        model=MODEL_NAME,
        messages=[message],
        max_tokens=100,
        stream=True)
    return stream

async def main():
    api_key = get_api_key("OPENAI_API_KEY")
    client = AsyncOpenAI(api_key=api_key)
    if api_key is not None:
        prompt = "Translate 'Hello, world!' into French."
        stream = await send_prompt(client, prompt)
        async for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")
    else:
        print("API key is not available.")

if __name__ == "__main__":
    asyncio.run(main())
