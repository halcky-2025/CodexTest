# CodexTest

## Extract Audio from Video

This repository includes a Python script `extract_audio.py` that allows you to select a video file and extract its audio.

### Setup

Install the required dependencies:

```bash
pip install moviepy imageio[ffmpeg]
```

### Usage

Run the script, passing the path to a video file:

```bash
python extract_audio.py /path/to/video.mp4
```

The audio track will be saved as an MP3 file in the same directory as the provided video. On systems without a graphical interface you can run the script with `xvfb-run` if needed:

```bash
xvfb-run python extract_audio.py /path/to/video.mp4
```
