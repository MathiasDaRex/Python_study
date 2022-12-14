# function = a block of code which is executed only when it is called

# we can use them with parameters
def helloParam(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age)+" "+"years old")
    print("Have a nice day!")

# or inputs defined inside the function
def helloInput():
    name = input("What is your name?")
    age = input("How old are you?")
    print("Hello "+name+"!")
    print("You are "+str(age)+" "+"years old")
    print("Have a nice day!")
    
    
#name = "Mathias"
#helloParam(name)
    
helloParam("Mathias","Rex",23)
helloInput()