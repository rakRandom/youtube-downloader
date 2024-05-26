import os
import time

try:
    from pytube import YouTube
except ImportError:
    raise ImportError("Error: pytube module was not found")


MAIN_PATH = "downloaded"  # Folder where the .mp4 will be after downloaded
LINK_PATH = "links.txt"   # Text file where will be the youtube links
WAIT_TIME = 60

class Main:
    def __get_name_list(self) -> tuple[str]:
        downloaded_files_names: list | set
        download_links: list | set
        name_list: tuple

        #
        downloaded_files_names = [
            file_name[:-4] 
            for file_name in os.listdir(MAIN_PATH) 
                if file_name[-4:] == ".mp4"
        ]
        
        #
        with open(LINK_PATH, 'r') as file: 
            download_links = [
                link 
                for link in file.read().split('\n')
                if len(link) > 0
                if link[0] != '#'
            ]

        try:
            # se o arquivo não foi baixado antes, e se não for um comentário (começar com '#')
            name_list = filter(lambda link: YouTube(link).title not in downloaded_files_names, download_links)
            name_list = tuple(set(name_list))
        except:
            print("log: cannot get name list")
            name_list = ()
        else:
            if name_list == ():
                print("log: name list empty")
            else:
                print("log: name list getted")
        finally:
            return name_list

    def __download_audio(self, name_list: tuple[str]) -> None:
        only_audio: bool

        for name in name_list:
            # Testing if it should be downloaded with or without video
            if name[0] == "$":
                only_audio = False
                name = name.split(' ')[1]
            else:
                only_audio = True
            
            # Trying to download
            yt = YouTube(name)
            try:
                print(f"log: downloading \"{yt.title}\"")
                audio = yt.streams.filter(only_audio=only_audio).first()
                audio.download(MAIN_PATH, f"{yt.title.lower().replace(' ', '-')}.mp4")
            except:
                print("log: was not possible download")
            else:
                print("log: audio download was successful")

    def verify_to_download(self):
        # obtendo a data da ultima modificação do arquivo
        last_modification = os.path.getmtime(LINK_PATH)
        self.__download_audio(self.__get_name_list())

        while True:
            print("log: iterating")

            # obtendo a data de modificação mais recente do arquivo
            newest_modification = os.path.getmtime(LINK_PATH)

            # verificando se a data de modificação mudou
            if newest_modification != last_modification:
                self.__download_audio(self.__get_name_list())
                last_modification = newest_modification

            # tempo de espera até verificar novamente
            time.sleep(WAIT_TIME)
