🎥 YouTube Downloader CLI ✨
A sleek, user-friendly command-line tool built in Python to download YouTube videos and playlists with support for audio language selection, subtitles, and custom video quality.

🚀 Features
✅ Flexible Downloads: Seamlessly download single videos or entire playlists.✅ Custom Quality: Select from a range of resolutions, from 360p to 4K.✅ Multilingual Audio: Choose your preferred audio language track (when available).✅ Auto-Embedded Subtitles: Automatically includes English (en) and Hindi (hi) subtitles, if available.✅ Progress Tracking: Enjoy a polished live progress bar with detailed download stats.

🎬 How It Works
1. Inspect Video OptionsPaste a YouTube URL, and the tool fetches available audio languages and subtitle options.
2. Select Language & QualityChoose your preferred audio language and video resolution.
3. Download with ProgressTrack your download with a dynamic progress bar.

📦 Requirements

Python 3.8+  
yt-dlp – Core library for downloading videos  
ffmpeg – Essential for merging audio/video and embedding subtitles


🛠️ Installation

Clone the Repository  
git clone https://github.com/joyboi-ai/Video-Downloader.git
cd Video-Downloader


Install Dependencies  
pip install -U yt-dlp
sudo apt update && sudo apt install ffmpeg

For non-Linux systems, download ffmpeg from ffmpeg.org/download.

Make the Script Executable  
chmod +x main.py
sudo ln -s "$(pwd)/main.py" /usr/local/bin/ytdl

Note: If ytdl isn’t recognized, restart your terminal or run source ~/.bashrc.



💡 Usage
Run the tool with:  
ytdl

You’ll be prompted to:  

Paste a YouTube video or playlist URL.  
Select your preferred audio language.  
Choose your desired video quality.  
Watch the download complete with embedded subtitles and a live progress bar!


❤️ Support the Project
If you love this tool, please give it a ⭐ on GitHub!Your support fuels further improvements and exciting new features.
