# *args = 	parameter that will pack all arguments into a tuple
#			useful so that a function can accept a varying amount of arguments

# tuples - ORDERED and UNCHANGEABLE

# defining 2 arguments, we must pass 2
# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# passing ALL the arguments, and packing them in a tuple
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# we can name *args as we want, the important thing is to have the asterisk (*) before it
def minus(*numberz):
    sum = 0
    # cuz it's a tuple, you cant change it's values
    # numberz[0] = 0
    
    # if we want to change it, we can convert it to a different collection
    # like a list, what's MUTABLE, and INTERCHANGEABLE
    numberz = list(numberz)
    numberz[0] = 0
    for i in numberz:
        sum -= i
    return sum


print(add(1,2,3,4,5))
print(minus(5,10,20,5))
