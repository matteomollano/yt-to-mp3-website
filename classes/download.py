from pytube import YouTube
from classes.AlbumArt import downloadThumbnail, addThumbnail
import ffmpeg, os

def downloadVideo(url: str, filename: str):
    """Downloads a youtube video as an mp4 file

    Args:
        url (str): a youtube video url
        filename (str): name that you want for the mp4
    """
    
    # Create a YouTube object to interact with
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    
    # Get the yt video to download
    video = yt.streams.filter().first()
   
    # Download the video as mp4
    mp4_filename = filename + '.mp4'
    video.download(filename=mp4_filename)
    
    return mp4_filename
    

def convertToMP3(filename: str):
    """Converts an mp4 file to an mp3 using ffmpeg

    Args:
        filename (str): filename/filepath of the mp4 to convert
    """
    
    input_file = ffmpeg.input(filename + '.mp4')
    output_file = ffmpeg.output(input_file, filename + '.mp3', q='0')
    ffmpeg.run(output_file)
    
    return f"{filename}.mp3"

    
def downloadSong(url:str, filename: str):
    """Provides a command line interface for downloading a YouTube video as an mp3 file

    Args:
        url (str): a youtube video url
        filename (str): name that you want for the mp3 file
    """
    
    # Download the song as an mp4
    mp4_filename = downloadVideo(url=url, filename=filename)
    
    # Convert the mp4 to an mp3
    mp3_filename = convertToMP3(filename=filename)
    
    # Remove the mp4 file from the directory
    os.remove(mp4_filename)
    
    return mp3_filename


def addYouTubeThumbnail(url:str, filename:str):
    """Adds a song's YouTube thumbnail to the mp3 file

    Args:
        url (str): a youtube video url
        filename (str): name of the downloaded mp3 file
    """
    # Download the video's thumbnail
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    videoID = yt.video_id
    thumbnailUrl = f"https://img.youtube.com/vi/{videoID}/maxresdefault.jpg"
    downloadThumbnail(thumbnail_url=thumbnailUrl)
    
    # Add the thumbnail as cover art to the mp3
    mp3_filename = filename + '.mp3'
    addThumbnail(filename=mp3_filename)