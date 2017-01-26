# Author: Kristen Findley
# Date: 25 January 2017
# Python: Version 2.7.12
# Description: script that copies recently edited files into a special folder

import os
import shutil
import datetime
import time

current_time = time.time()

folderA = "/home/kristen/Documents/TechAcademy/Python/FolderA/"
folderB = "/home/kristen/Documents/TechAcademy/Python/FolderB/"

for i in os.listdir(folderA):
    time_file = os.path.getmtime(folderA + i)
    if current_time - 86400 <= time_file:
        shutil.copy(folderA + i, folderB)

