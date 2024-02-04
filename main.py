from modules.imports import *
from modules.constants import *



class Main:
    def __get_name_list(self) -> tuple:
        downloaded_files_names: list | set
        download_links: list | set
        name_list: tuple

        #
        downloaded_files_names = [
            file_name[:-4] 
            for file_name in os.listdir(MAIN_PATH) 
                if file_name[-4:] == FILES_EXT
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


    def __download_audio(self, name_list: tuple, *, only_audio=True) -> None:
        for name in name_list:
            yt = YouTube(name)
            try:
                # log downloading
                print(f"log: downloading \"{yt.title}\"")
                audio = yt.streams.filter(only_audio=only_audio).first()
                audio.download(MAIN_PATH)
            except Exception as e:
                #log erro 'e'
                print("log: was not possible download")
            else:
                #log sucesso
                print("log: audio download was successful")


    def verify_to_download(self):
        # obtendo a data da ultima modificação do arquivo
        last_modification = os.path.getmtime(LINK_PATH)
        self.__download_audio(self.__get_name_list())

        while True:
            # obtendo a data de modificação mais recente do arquivo
            newest_modification = os.path.getmtime(LINK_PATH)

            # verificando se a data de modificação mudou
            if newest_modification != last_modification:
                self.__download_audio(self.__get_name_list())
                last_modification = newest_modification

            # tempo de espera até verificar novamente
            time.sleep(1)
