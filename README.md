# Auto Music Downloader

> "Some awesome quote!" - A wise man

<br>

## Why I created this?
My motivation started when I didn't even knew what programming was (a.k.a. a long time ago), and I wanted to listen music but I didn't have internet at the time. So why didn't I just download from a generic YouTube .mp3 downloader? Well, I used to use these generic downloaders, but they have lots of ads (and probably lots of virus), so I promissed myself that I would do one myself.

<br>

## What you need
- Python 3.12
- The hability to use the terminal
- Windows? idk, probably you can execute with Linux or MacOS
- motivation, I guess

<br>

## What you don't need
- A Virtual Environment, if you don't want to
- JDK, probably

<br>

## What features this have
You can download .mp4 files from YouTube, with or without video, just pasting the link of the video (or writing it, if you are some sort of psychopath) at `links.txt` file and waiting from 0 to 60 seconds.

`links.txt` looks like this, as you can see:
```text
# - write here the youtube videos url
# - save the file to start
# - already downloaded audios will not be downloaded again
# - '#' character is used to write comment lines, always as the first character
# - '$' character is used to download audio and video ($ https://youtube.com/[...])
```
So you can add comments with '#' character and a space before. The same thing when you want to download audio and video together, just use the '$' character and a space before.

<br>

## How to use
The main files of this project are `main.py`, `run.py`, `requirements.txt` and `links.txt`, but you don't have to open any of these except from `links.txt`.

First of all open the project folder at the terminal, it should look like this:
```cmd
C:\Users\GenericPeople\Downloads\auto-music-downloader>
```
Second of all, make sure that you have Python 3.12 downloaded and at the PATH. After that, execute this command at the terminal:
```cmd
pip install -r requirements.txt
```
Finally, run the `run.py` with this command:
```cmd
python run.py
```
Before all this, just paste all your links at the `links.txt` and have fun listening to your musics.

> Note:  If you have Python 3 and 2 installed, use `pip3` and `python3` instead of `pip` and `python`

<br>

## Some features that this project may need
- GUI
- Batch/Automation file to prepare the project to run
- README section teaching how to execute the script when the PC starts
- ...
