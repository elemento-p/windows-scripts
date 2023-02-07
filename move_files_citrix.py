# This script takes files out of sub-directories, moves them to
# a new directory and deletes the now empty folders.

# set root and destination if different than below.

from genericpath import exists
import os
import shutil
from pathlib import Path

rootFolder = 'c:/!Citrix/profile_import/move'
destination = 'c:/!Citrix/profile_import/destination'

# change working directory
os.chdir(rootFolder)

# go through sub-folders and move file to destination folder
totalFiles = 0
moveFiles = 0
deldir = 0

for dirpath, dirnames, filenames in os.walk(rootFolder):
    for filename in filenames:
        src = os.path.join(dirpath, filename)
        dest = os.path.join(destination, filename)
        if os.path.isfile(dest):
            print(f'{filename} already exists, skipping.')
            totalFiles += 1
        else:
            print(f'Moving {filename} to {destination}')
            shutil.move(src, destination)
            os.rmdir(dirpath)
            totalFiles += 1
            moveFiles += 1
            deldir += 1

print(f'\n \nSource: {rootFolder}' )
print(f'Destination: {destination} \n')
print(f'\n \nTotal files: {totalFiles}. \n')  
print(f'Moved {moveFiles} files \n') 
print(f'skipped {totalFiles - moveFiles} files. \n')
print(f'Deleted {deldir} directories. \n\n')
