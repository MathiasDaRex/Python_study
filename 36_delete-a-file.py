import os
import shutil

path = "test35.txt"
testtext = "Hi dude, you just created me"

# 	os.remove(path)		#delete a file
# 	os.rmdir(path)		#delete an empty directory
#	shutil.rmtree(path)	#delete a directory containing files


# try:
#     # remove function don't work on folders
#     os.remove('test36.txt')
#     print("File deleted")
# except FileNotFoundError:
#     print("That file was not found")
        

folderPath = "empty_folder"
try:
    # os.remove(path) <-	this does not work on folders
    # 						except we use rmdir
    # 						but also, it deletes only EMPTY folders
    # To delete folders with files in it, you have to use shutil
    # shutil.rmtree(path)<-	stands for REMOVE TREE
    #						That is a DANGEROUS function, because
    #						it will DELETE a directory and ALL of it's files
    
#	os.remove(path)
#   os.rmdir(folderPath)
    shutil.rmtree(folderPath)
except FileNotFoundError:
    print("That folder was not found, please create it in the root.")
except PermissionError:
    print("You don't have the permission to do that.")
except OSError:
    print("The folder is not empty, os.rmdir only deletes empty folders...")
else:
    print(folderPath+" was deleted")