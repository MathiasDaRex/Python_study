# **kwargs = 	parameter that will pack all arguments into a dictionary
#				useful so that a function can accept a varying amount of keyword arguments



# def hello(first, last):
#     print("Hello " + first + " " + last)
#     
# hello(first="Mathias", middle = "Da", last="Rex")
# this won't work because we haven't added middle argument to the function

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    
hello(first="Mathias", middle = "Da", last="Rex")

# if we want to display someones full name based on the amount of keyword arguments they passed
# like *args we can also name this as we like, the important thing is the ** before it

def hello_var(**names):
    print("Hello",end=" ")
    for key,value in names.items():
        print(value, end=" ")
    
hello_var(pre="Mr.",first="Mathias", middle = "Da", last="Rex", lastlast="Dude")
