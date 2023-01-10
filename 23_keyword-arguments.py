# keyword arguments = 	arguments preceded by an identifier when we pass them to a function
#						The order of the arguments doesn't matter, unlike positional arguments
#						Python knows the names of the arguments that our function recieves
#---------------------------------------------

# positional arguments - the order DOES matter
def henlo(first,middle,last):
     print("Hello "+first+" "+middle+" "+last)
    
henlo("Mathias","Da","Rex")

#---------------------------------------------

# keyword arguments - the order DOESN'T matter, because the preceded identifier
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)
    
hello(last="Rex",first="Mathias",middle="Da")
