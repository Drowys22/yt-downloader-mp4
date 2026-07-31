# Simple YouTube Downloader

A tiny Python script that uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download videos in the best available quality.

## Features

- Downloads the best available video + audio and merges them (falls back to the best combined format if needed)
- Saves files using the video's title as the filename
- Prompts you for a URL just press Enter to grab a demo video if you don't have one handy

## Requirements

- Python 3.7+
- [yt-dlp](https://pypi.org/project/yt-dlp/)
- [ffmpeg](https://ffmpeg.org/) (required by yt-dlp to merge separate video/audio streams)

## Installation

```bash
pip install yt-dlp
```

Make sure `ffmpeg` is installed and available on your system PATH.

## Usage

Run the script:

```bash
python downloader.py
```

You'll be prompted to enter a URL:

```
please enter a url to download:
```

- Paste any supported video URL and press Enter to start the download.
- Press Enter without typing anything to download a default sample video.

The downloaded file will be saved in the current directory, named after the video's title.

## Notes

- Only download content you have the right to download, and make sure your use complies with the terms of service of the site you're downloading from as well as applicable copyright law.
- Download speed and quality depend on the source site and your connection.

## Credits

Script by [Drowys22](https://github.com/Drowys22).
