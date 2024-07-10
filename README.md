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
<br>

## IF YOU RUN INTO PROBLEMS
If you run into a ```RegexMatchError: get_throttling_function_name: could not find match for multiple``` error or something similar, this is because the pytube library I am using has not been updated in over a year.<br><br>

In order to fix this problem, you need to change lines 272 and 273 in pytube's cipher.py from
```
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
```
to
```
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
```

<br>

cipher.py can be found at the following path in your project folder (your python version may differ):
```
myenv/lib/python3.9/site-packages/pytube/cipher.py
```