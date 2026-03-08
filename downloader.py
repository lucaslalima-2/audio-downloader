import yt_dlp
import argparse
import os
import shutil

def download_youtube_audio(url):
    """
    Downloads the best quality audio from a YouTube URL and converts it to MP3.
    """
    # 1. Ensure the downloads folder exists
    download_path = 'downloads'
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Check for FFmpeg
    if not shutil.which("ffmpeg"):
        print("❌ Error: FFmpeg not found.")
        return

    # 2. Configuration options
    # 'postprocessors' tells yt-dlp to convert the downloaded file to MP3 using FFmpeg
    ydl_opts = {
        'format': 'bestaudio/best',
        'paths': {'home': download_path},
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'source_address': '0.0.0.0', # Force IPv4
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'extractorargs': {
            'youtube': {
                'player_client': ['default', '-android_sdkless']
            }
        },
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'FFmpegMetadata', 'add_metadata': True},
        ],
    }

    try:
        print(f"--- Searching for: {url} ---")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Success! Audio downloaded and converted to MP3.")
    
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Error: Could not download video. {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 2. Setup Command Line Arguments
    parser = argparse.ArgumentParser(description="Download audio from a YouTube link.")
    parser.add_argument("url", help="The full YouTube URL (e.g., https://www.youtube.com/watch?v=...)")
    
    args = parser.parse_args()
    
    # 3. Run the downloader
    download_youtube_audio(args.url)