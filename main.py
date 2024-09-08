import os
import time


try:
    from pytubefix import YouTube
    from pytubefix import exceptions
    from pytubefix import Stream
except ImportError:
    print("Error: pytube module was not found")
    exit()

try:
    from config import main_path, link_path, wait_time
except:
    print("Error: could not load configuration variables")
    exit()


class Main:
    def __get_name_list(self) -> tuple[str]:
        downloaded_files_names: list | set
        download_links: list | set
        name_list: tuple

        #
        downloaded_files_names = [
            file_name[:-4] 
            for file_name in os.listdir(main_path) 
                if file_name[-4:] == ".mp4"
        ]
        
        #
        with open(link_path, 'r') as file: 
            download_links = [
                link 
                for link in file.read().split('\n')
                if len(link) > 0
                if link[0] != '#'
            ]

        try:
            # If the file was not downloaded before, and if it isn't a comment
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
            
            yt = YouTube(name)

            # Getting the streams
            streams = yt.streams.filter(only_audio=only_audio)
            stream: Stream | None
            
            # Getting one stream
            stream = streams.get_highest_resolution()
            if stream is None:
                print("log: could not get the highest resolution video")
                stream = streams.first()

            if stream is None:
                print("log: could not get any video resolution")
                return
            
            # Trying to download
            print(f"log: downloading \"{yt.title}\"")
            
            try:
                stream.download(main_path, f"{yt.title}.mp4")
            except exceptions.AgeRestrictedError:
                print("log: this video has age restriction")
                return
            except:
                print("log: was not possible the download")
            else:
                print("log: the download was successful")

    def verify_to_download(self):
        # Getting the last modification date of the link file
        last_modification = os.path.getmtime(link_path)
        self.__download_audio(self.__get_name_list())

        while True:
            print("log: iterating")

            # Getting the last modification date of the link file, again
            newest_modification = os.path.getmtime(link_path)

            # Checking if the date has changed
            if newest_modification != last_modification:
                self.__download_audio(self.__get_name_list())
                last_modification = newest_modification

            # Waiting until next iteration
            time.sleep(wait_time)
