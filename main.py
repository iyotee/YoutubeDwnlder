import yt_dlp
import subprocess
import os
import urllib.parse

def list_formats(url):
    ydl_opts = {
        'listformats': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            for f in formats:
                print(f"Format code: {f['format_id']}, Ext: {f['ext']}, Resolution: {f.get('resolution', 'N/A')}, Note: {f.get('format_note', 'N/A')}")
    except yt_dlp.utils.DownloadError as e:
        print(f"ERROR: {e}")

def get_best_format(formats, is_audio):
    best_format = None
    for f in formats:
        if is_audio:
            abr = f.get('abr', 0)
            if f.get('acodec') and (best_format is None or (abr is not None and abr > best_format.get('abr', 0))):
                best_format = f
        else:
            height = f.get('height')
            if height is not None:
                if best_format is None or (height > best_format.get('height', 0)):
                    best_format = f
    return best_format

def download_video(url, format_code, output_filename):
    ydl_opts = {
        'format': format_code,
        'outtmpl': output_filename,
        'retries': 10,  # Number of retries
        'timeout': 600,  # Timeout duration in seconds
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"ERROR: {e}")

def merge_audio_video(video_file, audio_file, output_file):
    # Command to merge audio and video using ffmpeg
    cmd = f"ffmpeg -i \"{video_file}\" -i \"{audio_file}\" -c:v copy -c:a aac -strict experimental \"{output_file}\""
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error merging audio and video: {e}")

def download_and_merge(url):
    # Get video and audio formats
    try:
        with yt_dlp.YoutubeDL({}) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])

            best_video_format = get_best_format(formats, is_audio=False)
            best_audio_format = get_best_format(formats, is_audio=True)

            if best_video_format:
                video_format_code = best_video_format['format_id']
            else:
                video_format_code = 'bestvideo'

            if best_audio_format:
                audio_format_code = best_audio_format['format_id']
            else:
                audio_format_code = 'bestaudio'

            print(f"Selected video format: {video_format_code}")
            print(f"Selected audio format: {audio_format_code}")

            # Temporarily set output filenames for video and audio
            video_filename = "temp_video.mp4"
            audio_filename = "temp_audio.m4a"

            # Download video and audio separately
            download_video(url, video_format_code, video_filename)
            download_video(url, audio_format_code, audio_filename)

            # Merge video and audio into final output file
            final_output = f"{os.path.splitext(video_filename)[0]}_merged.mp4"
            merge_audio_video(video_filename, audio_filename, final_output)

            # Get the original video title from YouTube info
            video_title = info_dict.get('title', 'video')
            video_title = urllib.parse.unquote(video_title)  # Decode URL encoding
            video_title = video_title.replace('/', '_')  # Replace '/' with '_'
            video_title = video_title.replace(':', '-')  # Replace ':' with '-'
            video_title = video_title.replace('\\', '')  # Remove backslashes
            video_title = video_title.strip()  # Strip leading/trailing whitespace

            # Rename the merged file with the original video title and extension
            os.rename(final_output, f"{video_title}.mp4")
            print(f"Merged file saved as: {video_title}.mp4")

    except yt_dlp.utils.DownloadError as e:
        print(f"Error getting video formats: {e}")

    # Clean up temporary files
    if os.path.exists(video_filename):
        os.remove(video_filename)
    if os.path.exists(audio_filename):
        os.remove(audio_filename)

def main():
    url = input("Enter the URL of the YouTube video: ")

    print("Available formats:")
    list_formats(url)

    # Download and merge video and audio
    download_and_merge(url)

    print("Download and merge completed successfully!")

if __name__ == "__main__":
    main()
import yt_dlp
import subprocess
import os
import urllib.parse

def list_formats(url):
    ydl_opts = {
        'listformats': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            for f in formats:
                print(f"Format code: {f['format_id']}, Ext: {f['ext']}, Resolution: {f.get('resolution', 'N/A')}, Note: {f.get('format_note', 'N/A')}")
    except yt_dlp.utils.DownloadError as e:
        print(f"ERROR: {e}")

def get_best_format(formats, is_audio):
    best_format = None
    for f in formats:
        if is_audio:
            abr = f.get('abr', 0)
            if f.get('acodec') and (best_format is None or (abr is not None and abr > best_format.get('abr', 0))):
                best_format = f
        else:
            height = f.get('height')
            if height is not None:
                if best_format is None or (height > best_format.get('height', 0)):
                    best_format = f
    return best_format

def download_video(url, format_code, output_filename):
    ydl_opts = {
        'format': format_code,
        'outtmpl': output_filename,
        'retries': 10,  # Number of retries
        'timeout': 600,  # Timeout duration in seconds
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"ERROR: {e}")

def merge_audio_video(video_file, audio_file, output_file):
    # Command to merge audio and video using ffmpeg
    cmd = f"ffmpeg -i \"{video_file}\" -i \"{audio_file}\" -c:v copy -c:a aac -strict experimental \"{output_file}\""
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error merging audio and video: {e}")

def download_and_merge(url):
    # Get video and audio formats
    try:
        with yt_dlp.YoutubeDL({}) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])

            best_video_format = get_best_format(formats, is_audio=False)
            best_audio_format = get_best_format(formats, is_audio=True)

            if best_video_format:
                video_format_code = best_video_format['format_id']
            else:
                video_format_code = 'bestvideo'

            if best_audio_format:
                audio_format_code = best_audio_format['format_id']
            else:
                audio_format_code = 'bestaudio'

            print(f"Selected video format: {video_format_code}")
            print(f"Selected audio format: {audio_format_code}")

            # Temporarily set output filenames for video and audio
            video_filename = "temp_video.mp4"
            audio_filename = "temp_audio.m4a"

            # Download video and audio separately
            download_video(url, video_format_code, video_filename)
            download_video(url, audio_format_code, audio_filename)

            # Merge video and audio into final output file
            final_output = f"{os.path.splitext(video_filename)[0]}_merged.mp4"
            merge_audio_video(video_filename, audio_filename, final_output)

            # Get the original video title from YouTube info
            video_title = info_dict.get('title', 'video')
            video_title = urllib.parse.unquote(video_title)  # Decode URL encoding
            video_title = video_title.replace('/', '_')  # Replace '/' with '_'
            video_title = video_title.replace(':', '-')  # Replace ':' with '-'
            video_title = video_title.replace('\\', '')  # Remove backslashes
            video_title = video_title.strip()  # Strip leading/trailing whitespace

            # Rename the merged file with the original video title and extension
            os.rename(final_output, f"{video_title}.mp4")
            print(f"Merged file saved as: {video_title}.mp4")

    except yt_dlp.utils.DownloadError as e:
        print(f"Error getting video formats: {e}")

    # Clean up temporary files
    if os.path.exists(video_filename):
        os.remove(video_filename)
    if os.path.exists(audio_filename):
        os.remove(audio_filename)

def main():
    url = input("Enter the URL of the YouTube video: ")

    print("Available formats:")
    list_formats(url)

    # Download and merge video and audio
    download_and_merge(url)

    print("Download and merge completed successfully!")

if __name__ == "__main__":
    main()
