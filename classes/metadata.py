import eyed3

def display_properties(filepath: str):
    audio_file = eyed3.load(filepath)
    print(f"Title: {audio_file.tag.title}")
    print(f"Artist: {audio_file.tag.artist}")
    
def update_properties(filename: str, title: str, artist: str):
    audio_file = eyed3.load(filename)
    audio_file.tag.title = title
    audio_file.tag.artist = artist
    audio_file.tag.save()