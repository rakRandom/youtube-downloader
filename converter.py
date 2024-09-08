""" File related to the convertion from MP4 to MP3

Converts a file from MP4 to MP3 and adds metadata to it
"""

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from moviepy.editor import AudioFileClip
from config import main_path
from os import remove

# Metadata things
def add_metadata(filename: str, title: str, album: str, album_artist: str, date: str):
    file = MP3(filename, ID3=EasyID3)

    file["title"] = [title]
    file["album"] = [album]
    file["albumartist"] = [album_artist]
    file["date"] = [date]

    file.save()


# MP3 to MP4 converter things
def mp3tomp4(filename, album: str, album_artist: str, date: str):
    mp4filename = f"{main_path}/{filename}.mp4"
    mp3filename = f"{main_path}/{filename}.mp3"

    # Load the mp4 file
    video = AudioFileClip(mp4filename)

    # Extract audio from video
    video.write_audiofile(mp3filename, logger=None)
    add_metadata(mp3filename, filename, album, album_artist, date)

    remove(mp4filename)
