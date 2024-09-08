""" Configuration file

Loads the variables needed by the main program from the config.json file

The config.json file needs to be in the same folder as this script
"""

import json

main_path: str = ""  # Folder where the .mp4 will be after downloaded
link_path: str = ""  # Text file where will be the youtube links
wait_time: int = 0   # Time in minutes from one iteration to another

with open("config.json", "r", encoding="UTF-8") as file:
    content = json.load(file)
    main_path = content["main_path"]
    link_path = content["link_path"]
    wait_time = content["wait_time"]

if main_path == "" or link_path == "" or wait_time == 0:
    raise Exception
