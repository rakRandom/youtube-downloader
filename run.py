""" Run file

Execute this file to run the program
"""

try:
    from config import main_path, link_path, wait_time
except:
    print("Error: could not load configuration variables")
    exit()

from main import Main
import os
import time


if __name__ == "__main__":
    main = Main(main_path, link_path)

    # Getting the last modification date of the link file
    last_modification = os.path.getmtime(link_path)
    main.download_audio(main.get_name_list())

    while True:
        print("log: iterating")

        # Getting the last modification date of the link file, again
        newest_modification = os.path.getmtime(link_path)

        # Checking if the date has changed
        if newest_modification != last_modification:
            main.download_audio(main.get_name_list())
            last_modification = newest_modification

        # Waiting until next iteration
        time.sleep(wait_time)
