import os

# check to see if a file exists somewhere on our computer

#path = "C:\\Users\\matyas.gyorke\\Desktop\\test.txt"
path = "C:\\Users\\matyas.gyorke\\Desktop\\folder"

if os.path.exists(path):
    print("That location exists!")
    # to check if it's a file
    if os.path.isfile(path):
        print("That is a file")
    # to check if it's a folder
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exists!")