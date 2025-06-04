# CodexTest

## Extract Audio from Video

This repository includes a Python script `extract_audio.py` that allows you to select a video file and extract its audio.

### Setup

Install the required dependencies:

```bash
pip install moviepy imageio[ffmpeg]
```

### Usage

Run the script:

```bash
python extract_audio.py
```

A file selection dialog will appear. Choose a supported video file (`.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`, `.flv`). The audio track will be saved as an MP3 file in the same directory as the selected video.
