import requests
import os

API_URL = "https://api-inference.huggingface.co/models/gpt2"


def call_ai(text):
    payload = {
        "inputs": text
    }

    r = requests.post(API_URL, json=payload)

    # HuggingFace bazen liste döner
    data = r.json()

    if isinstance(data, list) and "generated_text" in data[0]:
        return data[0]["generated_text"]
    else:
        return str(data)


def generate_scenes(text):
    prompt = f"""
Metni analiz et.
YouTube Shorts ve uzun video için ayrı sahneler üret.
Her sahne 2-3 saniye olsun.
JSON formatında dön.

Metin:
{text}
"""
    return call_ai(prompt)


def main():
    text = "Karanlık bir şehirde geçen anime horror hikayesi yaz."

    print("⏳ AI çalışıyor...")
    result = generate_scenes(text)

    print("\n✅ AI ÇIKTISI:\n")
    print(result)


if __name__ == "__main__":
    main()        size=(720, 1280)
    )

    # LONG
    long_images = []
    long_durations = []

    for s in scenes["long"]:
        img_path = f"output/images/long_{s['scene']}.png"
        download_placeholder(img_path)
        long_images.append(img_path)
        long_durations.append(s["duration"])

    create_video(
        long_images,
        long_durations,
        "output/videos/long.mp4",
        size=(1280, 720)
    )

    print("✅ Shorts ve Long video üretildi!")


if __name__ == "__main__":
    main()    result = r.json()[0]["generated_text"]
    return result

if __name__ == "__main__":
    text = input("Metni gir: ")
    output = generate_scenes(text)
    print(output)
