import os

if __name__ == "__main__":
    os.system("pip install pipreqs")
    os.system("pipreqs --force")
    os.system("pip install -r requirements.txt")
    os.system("cls")
else:
    from pytube import YouTube
