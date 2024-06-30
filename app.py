from flask import Flask, render_template, request, send_file, after_this_request
from classes.download import downloadSong, addYouTubeThumbnail
from classes.metadata import update_properties
from classes.AlbumArt import addCustomCoverArt
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get('url')
        title = request.form.get('title')
        artist = request.form.get('artist')
        cover_art_selection = request.form.get('cover-art-selection')
        
        # Download the mp3 file
        mp3_file = downloadSong(url=url, filename=title)
        
        # Update the file's metadata
        update_properties(filename=mp3_file, title=title, artist=artist)
        
        # Add cover art
        if cover_art_selection == "youtube-thumbnail":
            addYouTubeThumbnail(url=url, filename=title)
        elif cover_art_selection == "custom-cover-art":
            if 'custom-cover-art-file' in request.files:
                custom_cover_art_file = request.files['custom-cover-art-file']
                if custom_cover_art_file.filename:
                    addCustomCoverArt(mp3_filename=mp3_file, uploaded_cover_art=custom_cover_art_file)
        
        # Remove the mp3 file in our project directory after the send_file request is complete
        @after_this_request
        def remove_file(response):
            try:
                os.remove(mp3_file)
            except Exception as error:
                app.logger.error(f"Error removing or closing downloaded file handle: {error}")
            return response
        
        # Send the mp3 file to the browser for download
        return send_file(mp3_file, as_attachment=True, download_name=f"{title}.mp3")
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)