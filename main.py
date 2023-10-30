from modules.imports import *



class Main:
    def __init__(self):
        self.__path = "C:/Users/Pichau/Music/Downloads"
    

    def get_name_list(self) -> tuple:
        name_list: tuple
        files: list | set
        links: list | set

        files = [item[:-4] for item in os.listdir(self.__path) if item.count('.') > 0 and item[-3:] == 'mp4']
        with open(self.__path + "/links.txt", 'r') as file: links = file.read().split('\n')
        name_list = tuple(set(filter(lambda i: YouTube(i).title not in files, links)))

        return name_list


    def download_audio(self, name_list: tuple) -> None:
        for name in name_list:
            yt = YouTube(name)
            audio = yt.streams.filter(only_audio = True).first()

            try:
                audio.download(self.__path)
            except: pass
