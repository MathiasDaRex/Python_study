# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "mathias Rex"

if(name[0].islower()):
    print("First letter is lowercase:",name)
    name = name.capitalize()

# create a substring
# [START:STOP:STEP]
first_name = name[0:7].upper()
last_name = name [8:11]
last_character = name[-1]
    
print(name)
print(first_name)
print(last_name.capitalize())
print(last_character+(last_character*3)[1].upper()+last_character)