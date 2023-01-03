# **kwargs = 	parameter that will pack all arguments into a dictionary
#				useful so that a function can accept a varying amount of keyword arguments

# if we define how many arguments a method can accept, we cannot add more

# def hello(first, last):
#     print("Hello " + first + " " + last)
#     
# hello(first="Mathias", middle="Da" last="Rex")

# if we use **kwargs keyword we can add as many as we want
# to access the values, we have to call the key for that value from the dictionary

# to iterate through the values, we can use a for loop

def hello(**kwargs):
    #print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
    
hello(first="Mathias", middle="Da", last="Rex", afterlast="DUUDE", lastlastlast="THIS IS ADDED AFTER")