import os
import argparse
from moviepy.editor import VideoFileClip

def extract_audio(video_path: str):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"File not found: {video_path}")

    output_path = os.path.splitext(video_path)[0] + ".mp3"
    with VideoFileClip(video_path) as clip:
        if clip.audio is None:
            raise ValueError("The provided video has no audio track")
        clip.audio.write_audiofile(output_path)
    print(f"Audio saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Extract audio from a video file")
    parser.add_argument("video", help="Path to the video file")
    args = parser.parse_args()
    extract_audio(args.video)

if __name__ == "__main__":
    main()
