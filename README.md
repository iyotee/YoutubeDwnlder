<div align="center">
	<img src="image/OIG2.svg" alt="Logo" wigth="400" height="400">
</div>

# YouTube Video Downloader and Merger

## Description

This Python script allows you to download YouTube videos and audio separately, then merge them into a single file. It supports various video and audio formats and ensures that the best available quality is selected automatically. This script uses `yt-dlp` for downloading and `ffmpeg` for merging.

## Features

- List available video and audio formats for a given YouTube video URL.
- Download the highest quality video and audio formats separately.
- Merge the downloaded video and audio into a single file using `ffmpeg`.
- Rename the final output file to the video title.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- yt-dlp
- ffmpeg

You can install the required Python package using pip:

```bash
	pip install yt-dlp  
```

ffmpeg must also be installed on your system.


## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-downloader-merger.git
cd youtube-downloader-merger
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
```

3. Install required packages:

```bash
pip install yt-dlp
```

4. Run the script:

```bash
python main.py
```

Enter the URL of the YouTube video when prompted.

## Code Overview

list_formats(url)
Lists available formats for the given YouTube video URL. It displays format codes, extensions, resolutions, and notes.

get_best_format(formats, is_audio)
Selects the best format based on quality. For video formats, it chooses the highest resolution. For audio formats, it chooses the highest bitrate.

download_video(url, format_code, output_filename)
Downloads a video or audio file using the specified format code and saves it with the given filename.

merge_audio_video(video_file, audio_file, output_file)
Merges a video file and an audio file into a single output file using ffmpeg.

download_and_merge(url)
Handles the process of downloading and merging video and audio. It also renames the final output file to the video title.

main()
Main function that prompts the user for a YouTube video URL, lists available formats, and initiates the download and merge process.

## Troubleshooting

```bash
KeyError: 'acodec' or TypeError: '>' not supported between instances of 'NoneType' and 'int': Ensure that the yt-dlp and ffmpeg versions are up to date.  
```

These errors occur when certain format details are missing or invalid.


## License

This project is licensed under the MIT License. Iyotee - August 2024

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!
