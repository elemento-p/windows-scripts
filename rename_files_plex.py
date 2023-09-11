# This script renames video files to conform to plex seasons naming.
# and copies them into a different folder.

# set root and source_folder if different than below.

from genericpath import exists
import os
import shutil
from pathlib import Path

# working folders
source_folder = r'J:\Video Convert\Bi An Trong Nha Hat'
write_folder = r'J:\Video Convert\Renamed'


# Use this to strip Revision for upload

# change working directory
os.chdir(write_folder)


# go through sub-folders and move file to source_folder folder
totalFiles = 0
moveFiles = 0
iteration = 1


for dirpath, dirnames, filenames in os.walk(source_folder):
    for filename in filenames:
        # Set episode number to always be 2 digits
        if iteration < 10:
            file_number = str(0) + str(iteration)
        else:
            file_number = str(iteration)

        # plex season file name convention is ShowName – s02e17 – Optional_Info.ext
        new_filename = filename[:-7] + ' - s01e' + file_number + ' - (1999)' + '.mp4'
        
        src = os.path.join(dirpath, filename)
        dest = os.path.join(write_folder, new_filename)
        
        if os.path.isfile(dest):
            print(f'{filename} already exists, skipping.')
            totalFiles += 1
        else:
            print(f'Moving {filename} to {source_folder}')
            shutil.copy(src, dest)
            totalFiles += 1
            moveFiles += 1
        
        iteration += 1 
            
        
print(f'\n \nSource: {source_folder}' )
print(f'Destination: {write_folder} \n')
print(f'\n \nTotal files: {totalFiles}. \n')  
print(f'Moved {moveFiles} files \n') 
print(f'Skipped {totalFiles - moveFiles} files. \n')
