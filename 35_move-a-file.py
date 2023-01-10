import os

source = "test35.txt"
# we can use this to folders as well
#sourcefolder = "folder35"

destination = "C:\\Users\\matyas.gyorke\\Desktop\\pyDest\\test35.txt"
#folderdestination = "C:\\Users\\matyas.gyorke\\Desktop\\pyDest\\folder35"

try:
    if os.path.exists(destination):
        print("There is already a file by that name")
#         os.replace(destination,source) to move back 
#         print("File moved back dude")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except fileNotFoundError:
    print(source +" was not found")