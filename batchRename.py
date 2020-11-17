# Python code to bulk rename multiple files in dir or folder (Python 3.6 on Linux)
# Adds corresponding sequence starting with index 0, program appends this digit
# To the a custom string the user has provided.

# Future updates should include a tkinter gui with text boxes and a drag drop section
# the program gui is cleaner. the plan is to have the user select/enter their filetype
# from a list of file extensions. Then enter their main filename into the textbox.
# Afterwards the program extract the filepaths from each individual file and rename them
# without program needing to be in the same directory as the files.

# Kevin Yeung Sept 1 2018

import os
import pathlib

# String path of current script and files in directory
path = pathlib.Path(__file__).parent.absolute()
files = os.listdir(path)

# Get filecount
for tempIndex, tempName in enumerate(files):
    total = tempIndex
total += 1

# Get renaming customization from user
try:
    print("conn0r says hello") #uh
    fileType = input("Enter the filetype extension (if any) for the files to be renamed, ex: .o or .bat: ")
    newName = input("Enter the main (if any) name for the new files, ex: name0, name1... or file_0, file_1...: ")

    # Iterate and get name/filepath for renaming
    for index, file in enumerate(files):

        # So program doesn't delete/rename itself
        if file == "bulkRename.py":
            print("skipping renaming program file")
        else:
            # os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), fileType]))) # Save for future
            os.rename(os.path.join(path, file), os.path.join(path, ''.join([newName, str(index), fileType])))
            print("Renaming file ", index, " of ", total, "[", file, " >>> ", newName, index, fileType, "]")

    print("Process complete, please check your directory. if an error occurred ... (ctrl-z) ;)")

except nameError:
    print("Filetype error, check your extensions and try again")
