import os

# directory of file to be renamed
path = r"C:\Users\dsmith\Downloads\MS Project Class\2 Exercise"
# File to be renamed
file = r"1.2inprogress+Project+Exercise+1+-+Birthday+Party+Plan+-+RESOURCE+ALLOCATIONS.mpp"
# path and file name joined

# Replace + with spaces in file name
new_file = file.replace("+", " ")

Old_full_path = os.path.join(path, file)
New_Full_path = os.path.join(path, new_file)

os.rename(Old_full_path, New_Full_path)