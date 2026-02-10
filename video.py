from moviepy.editor import ImageClip, concatenate_videoclips
import os

def create_video(images, durations, output_path, size):
    clips = []

    for img, dur in zip(images, durations):
        clip = ImageClip(img).set_duration(dur).resize(size)
        clips.append(clip)

    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(output_path, fps=24)
