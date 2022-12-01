# This script creates folders in a specified directory and numbers them.
import os, os.path
# from pathlib import Path

# get path of location to create folders
def get_path():
    # ask for path of directory to place folders and check input
    user_input_check = 0
    while user_input_check != 1:
        folder_path = input(r'Enter path where new folders will be placed: ')
        if os.path.exists(folder_path) == False:
            print('Path does not exist please re-enter. \n')
            folder_path = input(r'Enter path where new folders will be placed: ')
        print() # line break
        user_input = input('Is this correct? (Y/N): ')
        print() # line break
        user_input = user_input.lower()
        # check user y or n input
        while True:
            if user_input == 'y':
                user_input_check = 1
                break
            elif user_input == 'n':
                user_input_check = 0
                break
            else:
                user_input = input(f'Please enter Y or N: ')
    return folder_path

# set name of folders, ie sub 1, sub 2, sub 3, name = sub
def get_name():
    user_input_check = 0
    while user_input_check != 1:
        name = input(f'Enter new folders name: ')
        print() # line break
        user_input = input('Is this correct? (Y/N): ')
        print() # line break
        
        while True:
            user_input = user_input.lower()
            if user_input == 'y':
                user_input_check = 1
                break
            elif user_input == 'n':
                user_input_check = 0
                break
            else:
                user_input = input(f'Please enter Y or N: ') 
    return name

# set folder numbering, ie sub 1, sub 2, sub 3, start = 1 end = 3
def get_number():
    # get starting and ending number.
    while True:
        # make sure entry is an integer
        try:
            number_start = int(input('Enter the starting number for the folder name: '))
            print() # line break
        except ValueError:
            print("Enter a number.")
            continue
        # make sure entry is an integer
        try:
            number_end = int(input('Enter the ending number for the folder name: '))
            print() # line break
        except ValueError:
            print("Enter a number")
            print() # line break
            continue
        # check is start is smaller than end
        if number_start <= number_end:
            break
        else: 
            print('Your starting number should be smaller than your ending number. \n') # includes line break
    return number_start, number_end
        
# create folders
def make_folders(path, name, number_start, number_end):
    # create list of folder numbers, inclusive of start and end
    folder_range = [*range(number_start, number_end+1, 1)]
    folder_name = [name + f' ' + str(s) for s in folder_range]
    # change directory
    os.chdir(path)
    # make folders
    for i in folder_name:
        try:
            os.makedirs(os.path.join(path, i))
        except OSError:
            pass
    return


# program start
user_input_check = 0
while user_input_check != 1:
    path = get_path()
    name = get_name()  
    number_start ,number_end = get_number()
    # calculate total number of folders created
    total_number_folders = number_end - number_start + 1
    # final confirmation before folder creation
    print(f'\nYou entered: \n Path: {path} \n Folder Name: {name} \n Starting Number: {number_start} \n Ending Number: {number_end}\n')
    print(f'This will create {total_number_folders} folders.')
    print()
    user_input = input('Is this correct? (Y/N): ')
    user_input = user_input.lower()
    # check user input
    while True:
        if user_input == 'y':
            user_input_check = 1
            break
        elif user_input == 'n':
            user_input_check = 0
            break
        else:
            user_input = input(f'Please enter Y or N: ')
    
    
    
# create folders
make_folders(path, name, number_start, number_end)

   