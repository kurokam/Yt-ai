from scenes import generate_scenes
from video import create_video
import os

# Geçici placeholder görseller
PLACEHOLDER_IMAGE = "https://via.placeholder.com/720x1280.png"

def download_placeholder(path):
    import requests
    r = requests.get(PLACEHOLDER_IMAGE)
    with open(path, "wb") as f:
        f.write(r.content)


def main():
    os.makedirs("output/images", exist_ok=True)
    os.makedirs("output/videos", exist_ok=True)

    text = "Karanlık bir şehirde geçen gizemli bir anime horror hikayesi."

    scenes = generate_scenes(text)

    # SHORTS
    shorts_images = []
    shorts_durations = []

    for s in scenes["shorts"]:
        img_path = f"output/images/short_{s['scene']}.png"
        download_placeholder(img_path)
        shorts_images.append(img_path)
        shorts_durations.append(s["duration"])

    create_video(
        shorts_images,
        shorts_durations,
        "output/videos/shorts.mp4",
        size=(720, 1280)
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
