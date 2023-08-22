# find all files of specific type in directory tree
# copy to a new folder and keep newest copy

import os, glob, shutil

# source and destination directories
src = r'C:\source_files_folder'
dest = r'C:\destination_files_folder'

os.chdir(src)

# get all files of specific type in the entire directory tree (recursive= sets this)
src_res = glob.glob('**/*.docx', recursive=True)

# iterate over list           
for file in src_res:
    file_name = os.path.basename(file)                  # get the file name only
    abs_path = src + '\\' + file                        # get full path of source file. Need \\ to join the src path and file name 
    dest_name = os.path.join( dest + '\\' + file_name)  # get full path of destination
    # check if file exists at destination and copy OR check the file modification time. if newer copy
    if (not os.path.exists(dest_name)) or (os.stat(file).st_mtime - os.stat(dest_name).st_mtime > 1):
        shutil.copy2(abs_path,dest_name)                # copy file if conditions met
    