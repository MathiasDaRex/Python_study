# copyfile() = 	copies contents of a file
# copy() = 		copyfile() + permission mode + destination can be a directory
# copy2() = 	copy() + copies metadata (file's creation and modification times)

# copy() and copy2() have exactly the same arguments
# copy(src,dst), copy2(src,dst)

import shutil

# if file is in the project folder
# shutil.copyfile('text.txt','copy.txt') # src,dst

# if destination file is other
shutil.copyfile('text.txt','C:\\Users\\matyas.gyorke\\Desktop\\pyDest\\copy.txt')