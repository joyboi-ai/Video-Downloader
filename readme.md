YouTube Downloader CLI ✨A simple, yet powerful command-line tool built in Python to download YouTube videos and playlists with audio language and quality selection.Features 🚀Download anything: Grab single videos or entire playlists with ease.Quality control: Select your desired video resolution from low (360p) up to crystal-clear 4K.Multilingual audio: Choose a preferred audio language track if available.Smart subtitles: Automatically embeds English (en) and Hindi (hi) subtitles, if they exist for the video.How it Looks 🎬Here's a glimpse of the tool in action:1. Inspecting Video Languages(After pasting a video URL, it fetches available audio and subtitle options)2. Language and Quality Selection(Choosing audio language and video resolution)3. Downloading with Progress(Visualizing the download progress)Requirements 📦Python 3.x: The script is written in Python.yt-dlp: The powerful backbone for video downloading.ffmpeg: Essential for merging video and audio streams, and embedding subtitles.Installation 🛠️Clone the repository:git clone [https://github.com/joyboi-ai/Video-Downloader.git](https://github.com/joyboi-ai/Video-Downloader.git)
cd Video-Downloader
Install dependencies:yt-dlp:pip install -U yt-dlp
ffmpeg:# On Debian/Ubuntu-based systems (like Pop!_OS)
sudo apt update && sudo apt install ffmpeg
# For other operating systems, please refer to ffmpeg.org/download.html
Make the script executable and create a global command:chmod +x main.py
# This creates a symbolic link, allowing you to run 'ytdl' from any directory
sudo ln -s "$(pwd)/main.py" /usr/local/bin/ytdl
Note: You might need to open a new terminal or run source ~/.bashrc if ytdl isn't immediately recognized.Usage 💡Simply run the command in your terminal:ytdl
The script will interactively guide you through entering the YouTube URL, selecting your preferred audio language, and choosing the video quality.Star This Repo! ⭐If you find this tool helpful, please consider giving it a star on GitHub! It greatly helps in visibility and motivates further development.License 📄This project is licensed under the MIT License.
