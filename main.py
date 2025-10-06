import subprocess
import os
import shutil

def check_for_yt_dlp():
    """Checks if yt-dlp is installed and in the system's PATH."""
    if not shutil.which("yt-dlp"):
        print("--- ERROR ---")
        print("`yt-dlp` is not found on your system.")
        print("Please install it before running this script: pip install -U yt-dlp")
        print("Also ensure `ffmpeg` is installed: sudo apt install ffmpeg")
        return False
    # Check for ffmpeg as well, as it's crucial for merging audio/video
    if not shutil.which("ffmpeg"):
        print("--- WARNING ---")
        print("`ffmpeg` is not found on your system. `yt-dlp` needs it to merge video and audio.")
        print("You can install it with: sudo apt install ffmpeg")
        print("Downloads might be video-only or audio-only if `ffmpeg` is missing.")
    return True

def get_quality_format_string():
    """
    Presents a simplified quality selection menu and returns the
    corresponding yt-dlp format string for best video+audio.
    """
    print("\nSelect desired video quality:")
    print("  1) Low (Max 360p)")
    print("  2) Medium (Max 720p)")
    print("  3) High (Max 1080p)")
    print("  4) 2K (Max 1440p)")
    print("  5) 4K (Max 2160p)")
    print("  6) Best available (Default)")
    
    while True:
        choice = input("Enter your choice (1-6, or Enter for default): ").strip()
        
        if not choice or choice == '6':
            print("Selected: Best available quality.")
            return "bestvideo+bestaudio/best"

        if choice == '1':
            print("Selected: Low (Max 360p)")
            return "bestvideo[height<=360]+bestaudio/best[height<=360]"
        elif choice == '2':
            print("Selected: Medium (Max 720p)")
            return "bestvideo[height<=720]+bestaudio/best[height<=720]"
        elif choice == '3':
            print("Selected: High (Max 1080p)")
            return "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
        elif choice == '4':
            print("Selected: 2K (Max 1440p)")
            return "bestvideo[height<=1440]+bestaudio/best[height<=1440]"
        elif choice == '5':
            print("Selected: 4K (Max 2160p)")
            return "bestvideo[height<=2160]+bestaudio/best[height<=2160]"
        else:
            print("Invalid choice. Please enter a number from 1 to 6, or press Enter.")

def download_video():
    """Handles the download process for a single video."""
    video_url = input("Enter the YouTube video URL: ")
    format_string = get_quality_format_string()
    
    download_path = os.path.join("Downloads", "Video")
    os.makedirs(download_path, exist_ok=True)
    
    download_command = [
        "yt-dlp",
        "--progress",
        "-f", format_string,
        "-o", os.path.join(download_path, "%(title)s.%(ext)s"),
        video_url
    ]
    
    print(f"\nStarting download... (File will be saved in '{download_path}')")
    try:
        subprocess.run(download_command, check=True)
        print("\n✅ Download complete!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Download failed. yt-dlp returned an error. Details: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred during download: {e}")

def download_playlist():
    """Handles the download process for a YouTube playlist."""
    playlist_url = input("Enter the YouTube playlist URL: ")
    format_string = get_quality_format_string()
    
    # Define the full output path template for yt-dlp
    # This single string tells yt-dlp to create the folders and name the files correctly
    output_template = os.path.join("Downloads", "Playlists", "%(playlist)s", "_%(playlist_index)03d : %(title)s.%(ext)s")
    
    # Construct the download command
    download_command = [
        "yt-dlp",
        "--progress",
        "--concurrent-fragments", "3", # Use 3 threads for downloading
        "-f", format_string,
        "-o", output_template, # Use the full combined output template
        "--yes-playlist",
        playlist_url
    ]

    print(f"\nStarting playlist download with 3 threads...")
    print(f"(Videos will be saved in a subfolder inside 'Downloads/Playlists')")
    try:
        subprocess.run(download_command, check=True)
        print("\n✅ Playlist download complete!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Playlist download failed. yt-dlp returned an error. Details: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred during playlist download: {e}")

def main():
    """Main function to run the application."""
    if not check_for_yt_dlp():
        return

    print("--- YouTube Downloader (Powered by yt-dlp) ---")
    while True:
        print("\nWhat would you like to download?")
        print("  1) A single video")
        print("  2) An entire playlist")
        print("  3) Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            download_video()
        elif choice == '2':
            download_playlist()
        elif choice == '3':
            print("Exiting application. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()