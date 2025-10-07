# YouTube Downloader CLI ✨

A simple, yet powerful command-line tool built in Python to download YouTube videos and playlists with audio language and quality selection.

---

## Features 🚀

* **Download anything:** Grab single videos or entire playlists with ease.
* **Quality control:** Select your desired video resolution from low (360p) up to crystal-clear 4K.
* **Multilingual audio:** Choose a preferred audio language track if available.
* **Smart subtitles:** Automatically embeds English (`en`) and Hindi (`hi`) subtitles, if they exist for the video.

## How it Looks 🎬

Here's a glimpse of the tool in action:

**1. Inspecting Video Languages** (After pasting a video URL, it fetches available audio and subtitle options)

![App inspecting video languages](./output/1.png)

**2. Language and Quality Selection** (Choosing audio language and video resolution)

![App language and quality selection](./output/2.png)

**3. Downloading with Progress** (Visualizing the download progress)

![App downloading with progress bar](./output/3.png)

## Requirements 📦

* **Python 3.x**: The script is written in Python.
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp): The powerful backbone for video downloading.
* [`ffmpeg`](https://ffmpeg.org/): Essential for merging video and audio streams, and embedding subtitles.

---

## Installation 🛠️

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/joyboi-ai/Video-Downloader.git](https://github.com/joyboi-ai/Video-Downloader.git)
    cd Video-Downloader
    ```

2.  **Install dependencies:**
    * **`yt-dlp`**:
        ```bash
        pip install -U yt-dlp
        ```
    * **`ffmpeg`**:
        ```bash
        # On Debian/Ubuntu-based systems (like Pop!_OS)
        sudo apt update && sudo apt install ffmpeg
        # For other operating systems, please refer to ffmpeg.org/download.html
        ```

3.  **Make the script executable and create a global command:**
    ```bash
    chmod +x ytdl.py
    # This creates a symbolic link, allowing you to run 'ytdl' from any directory
    sudo ln -s "$(pwd)/ytdl.py" /usr/local/bin/ytdl
    ```
    **Note:** You might need to open a new terminal or run `source ~/.bashrc` if `ytdl` isn't immediately recognized.

---

## Usage 💡

Simply run the command in your terminal:

```bash
ytdl