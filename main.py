from modules.imports import *
from modules.constants import *



class Main:
    def get_name_list(self) -> tuple:
        name_list: tuple
        files: list | set
        links: list | set

        files = [item[:-4] for item in os.listdir(MAIN_PATH) if item[-4:] == FILES_EXT]
        with open(LINK_PATH, 'r') as file: links = file.read().split('\n')
        name_list = tuple(set(filter(lambda i: YouTube(i).title not in files, links)))

        return name_list


    def download_audio(self, name_list: tuple) -> None:
        for name in name_list:
            yt = YouTube(name)
            audio = yt.streams.filter(only_audio = True).first()

            try:
                audio.download(MAIN_PATH)
            except: pass
