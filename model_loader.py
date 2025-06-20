import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load HF_TOKEN from .env
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# Create inference client using "together" provider
client = InferenceClient(
    provider="together",
    api_key=HF_TOKEN,
)

def query_chat(messages, model="mistralai/Mistral-7B-Instruct-v0.3"):
    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return completion.choices[0].message.content

