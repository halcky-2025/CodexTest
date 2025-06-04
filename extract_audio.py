import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def select_and_extract():
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv *.webm *.flv")]
    )
    if not video_path:
        print("No file selected.")
        return

    output_path = os.path.splitext(video_path)[0] + ".mp3"
    with VideoFileClip(video_path) as clip:
        clip.audio.write_audiofile(output_path)
    print(f"Audio saved to {output_path}")

if __name__ == "__main__":
    select_and_extract()
