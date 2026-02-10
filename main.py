import os
import requests
import json

HF_TOKEN = os.environ["HF_TOKEN"]

LLM_MODEL = "Qwen/Qwen2.5-7B-Instruct"
API_URL = f"https://api-inference.huggingface.co/models/{LLM_MODEL}"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def generate_scenes(text):
    prompt = f"""
Metni analiz et.
YouTube Shorts ve uzun video için ayrı sahneler üret.
Her sahne 2-3 saniye olsun.
JSON formatında dön.

Metin:
{text}
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 700,
            "temperature": 0.7
        }
    }

    r = requests.post(API_URL, headers=headers, json=payload)
    r.raise_for_status()

    result = r.json()[0]["generated_text"]
    return result

if __name__ == "__main__":
    text = input("Metni gir: ")
    output = generate_scenes(text)
    print(output)
