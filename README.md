# yt to mp3 website
This is a website that allows you to download songs from YouTube. It was developed using HTML/CSS/JS and Python Flask. <br><br>

## Prerequisites
This application requires python3 and ffmpeg. <br>

### Manual Installation:
```
# Python Download
https://www.python.org/downloads/

# Download a static binary from ffmpeg's website, and add the binary to your path
https://www.ffmpeg.org/download.html
```

### Installation via Homebrew:
```
# Python
brew install python

# ffmpeg
brew install ffmpeg
```
<br>

## How to use this website
1. Download the git repository using the following command <br>
```
git clone https://github.com/matteomollano/yt-to-mp3-website.git
```

2. Navigate inside the project folder and create a virtual environment <br>
```
python3 -m venv myenv
```

3. You should now see a myenv directory in your project folder. Activate the virtual environment <br>
```
source myenv/bin/activate
```

4. Install the requirements <br>
```
pip3 install -r requirements.txt
```

5. Run app.py to start the Flask server <br>
```
python3 app.py
```

6. Open a web browser and go to the following <br>
```
localhost:5000
```

7. Enter the YouTube URL, song name, and artist name for the song that you want to download. You can also choose to use the YouTube video thumbnail as cover art, upload a custom cover art, or use no cover art <br>
```
The song will now download as an mp3 to your downloads folder!
```