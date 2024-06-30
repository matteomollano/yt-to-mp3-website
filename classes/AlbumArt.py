import urllib.request, eyed3, mimetypes, os
from eyed3.id3.frames import ImageFrame
from PIL import Image

def downloadThumbnail(thumbnail_url: str):
    """Downloads a youtube video's thumbnail as a jpg

    Args:
        thumbnail_url (str): a link to a youtube video's thumbnail
        Ex: https://img.youtube.com/vi/{videoID}/maxresdefault.jpg
        where videoID is the ID string associated with a given youtube video
    """
    
    urllib.request.urlretrieve(thumbnail_url, "thumbnail.jpg")
    
    
def makeSquare(thumbnail_filename: str):
    """Creates a new square thumbnail to be used for album cover art
       (crops a regular sized youtube thumbnail)

    Args:
        thumbnail_filename (str): filename/filepath to a youtube thumbnail
    """
    
    # Open the original thumbnail file
    original_image = Image.open(thumbnail_filename)

    # Calculate the size for the square thumbnail
    thumbnail_size = min(original_image.size)

    # Crop the center portion to create a square thumbnail
    left = (original_image.width - thumbnail_size) // 2
    top = (original_image.height - thumbnail_size) // 2
    right = left + thumbnail_size
    bottom = top + thumbnail_size
    square_thumbnail = original_image.crop((left, top, right, bottom))
    
    # Save the square thumbnail
    square_thumbnail.save('square_thumbnail.jpg')
    

def addThumbnail(filename: str):
    """Adds YouTube thumbnail as cover art to an mp3 file

    Args:
        filename (str): filename/filepath of the mp3 file
    """
    
    audiofile = eyed3.load(filename)
    print(audiofile)
    
    makeSquare(thumbnail_filename='thumbnail.jpg')
    
    if audiofile.tag is None:
        audiofile.initTag()
        
    with open ("square_thumbnail.jpg", "rb") as img_file:
        audiofile.tag.images.set(
            ImageFrame.FRONT_COVER, # 3 is the code for front cover art
            img_file.read(), # open the binary data of the cover art
            'image/jpeg' # mime type of the file
        )
        
    audiofile.tag.save()
    
    # Remove the two thumbnail images
    try:
        os.remove("thumbnail.jpg")
        os.remove("square_thumbnail.jpg")
    except:
        print("File could not be deleted")
    

def addCustomCoverArt(mp3_filename: str, uploaded_cover_art):
    """Adds a custom cover art to an mp3 file

    Args:
        mp3_filename (str): filename/filepath of the mp3
        uploaded_cover_art (werkzeug.datastructures.FileStorage): the uploaded file object
    """
    
    audiofile = eyed3.load(mp3_filename)
    print(audiofile)
    
    if audiofile.tag is None:
        audiofile.initTag()
        
    mime_type, _ = mimetypes.guess_type(uploaded_cover_art.filename)
    if mime_type:
        audiofile.tag.images.set(
            ImageFrame.FRONT_COVER,
            uploaded_cover_art.read(),
            mime_type
        )
    else:
        print(f"Warning: Could not determine MIME type for {uploaded_cover_art.filename}")
        print("Cover art was not added")
        
    audiofile.tag.save()