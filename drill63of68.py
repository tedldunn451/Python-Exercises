# Author: Kristen Findley
# Date: 25 January 2017
# Python: Version 2.7
# Description: File mover - program to move all .txt files from Folder A to Folder B.

import shutil
import os

folderA = "/home/kristen/Documents/TechAcademy/Python/FolderA/"
folderB = "/home/kristen/Documents/TechAcademy/Python/FolderB/"

for i in os.listdir(folderA):
    if i.endswith(".txt"):
        print folderB + i
        shutil.move(folderA + i,folderB)



        
