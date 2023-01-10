
# using with open - automaticly closes your file after using
# however this does not handle any exceptions that might occur
# like when we mistype the file name, that will cause a file not found error

# with open('text.tx') as file: # it's in the root folder
#     print(file.read())
# 
# print(file.closed)

try:
    with open('text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
    