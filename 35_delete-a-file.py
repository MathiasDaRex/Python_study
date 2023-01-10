import os

path = "test35.txt"

try:
    os.remove('test35.txt')
    print("File deleted")
except FileNotFoundError:
    print("That file was not found")