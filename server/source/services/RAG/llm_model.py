import openai
import os

import dotenv
dotenv.load_dotenv()

def get_response_completion(messages, max_tokens=512, model="meta-llama/Llama-3.3-70B-Instruct-Turbo"):
    client = openai.OpenAI(
        api_key = os.getenv("TOGETHER_API_KEY"),
        base_url = "https://api.together.xyz/v1",
    )
        
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        max_tokens=max_tokens,
        stop=[
            "<step>"
        ],
        frequency_penalty=1,
        presence_penalty=1,
        top_p=0.7,
        n=10,
        temperature=0.7,
    )

    return chat_completion
