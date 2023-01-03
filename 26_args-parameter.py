# *args = 	parameter that will pack all arguments into a tuple (tuples are ordered and unchangeable)
# 			useful so that a function cann accept a varying amount of arguments


# With this method we can only pass the predefined amount of arguments
#def add(x1,x2):
#    sum = x1 + x2
#    return sum

#print(add(2,3))

# with *args we can pass as many as we want
# we don'n have to name it args neccessarily, the most important thing is the  *  before it

# def add(*args):
#     sum = 0
#     for i in args:
#          sum += i
#     return sum

def add(*stuff):
    sum = 0
#    stuff[1] = 1 			  tuples are unchangeable 	to change it's values we have to cast it in some other collection, like a list
    stuff = list(stuff) 	# casting the stuff tuple to list
    stuff[4] = 0 			# now we can change the values
    for i in stuff:
         sum += i
    return sum


print(add(1,2,3,4,5,6,7,8,9,10))