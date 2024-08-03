import os
import re
import asyncio
import requests
from yt_dlp import YoutubeDL

# Hardcoded directory paths
THUMBNAIL_SAVE_PATH = "/path/to/file/Channel"
VIDEO_SAVE_PATH = "/path/to/file/Channel"
CHANNEL_URL = "https://www.youtube.com/@channel/videos"

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Ensure directories exist
ensure_directory_exists(THUMBNAIL_SAVE_PATH)
ensure_directory_exists(VIDEO_SAVE_PATH)

def sanitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

async def fetch_and_download_latest_video(channel_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
        'playlistend': 1,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(channel_url, download=False)
        entries = info_dict.get('entries', [])

        for entry in entries:
            video_url = entry['url']
            video_title = entry['title']

            # Check if the video is a short by looking at its duration
            video_info = ydl.extract_info(video_url, download=False)
            if video_info['duration'] < 60:
                print(f"Skipping short video (duration < 60s): {video_title}, URL: {video_url}")
                continue

            sanitized_title = sanitize_filename(video_title)
            thumbnail_url = video_info['thumbnail']
            video_path = os.path.join(VIDEO_SAVE_PATH, f"{sanitized_title}.mp4")
            thumbnail_path = os.path.join(THUMBNAIL_SAVE_PATH, f"{sanitized_title}.jpg")

            # Download the thumbnail
            download_thumbnail(thumbnail_url, thumbnail_path)

            # Download the video
            download_video(video_url, video_path)

            return

        print("No suitable videos found on the channel page.")

def download_thumbnail(thumbnail_url, save_path):
    print(f"Downloading thumbnail from {thumbnail_url} to {save_path}")
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        if os.path.exists(save_path):
            print(f"Verified: Thumbnail exists at {save_path}")
        else:
            print(f"Error: Thumbnail does not exist at {save_path}")
    else:
        print(f"Failed to download thumbnail from {thumbnail_url}")

def download_video(video_url, save_path):
    ydl_opts = {
        'outtmpl': save_path,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    if os.path.exists(save_path):
        print(f"Verified: Video exists at {save_path}")
    else:
        print(f"Error: Video does not exist at {save_path}")

async def main():
    try:
        await fetch_and_download_latest_video(CHANNEL_URL)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
