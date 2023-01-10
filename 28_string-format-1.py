# str.format() = 	optional method that gives users
#					more control when displaying output

# {} 	= 	format field

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)

# a more elegant way to write this
# curly braces {} are function as placeholders forvalues or variables
# {}-s are always goes from the first to the last
print("The {} jumped over the {}".format(animal,item))

# but we can also position them with indexes
print("The {1} jumped over the {0}".format(animal,item)) # positional arguments

# also we can use keyword arguments
print("The {animal} jumped over the {item}".format(animal="horse",item="fence")) # keyword arguments
# with this we can re-use the arguments multiple times
print("The {animal} jumped over the {animal}".format(animal="horse",item="fence")) # keyword arguments

# There is an EVEN MORE ELEGANT way
text = "The {} jumped over the {}"
print(text.format(animal, item))

print()
print()

# How to add some padding to a string when we display it
name = "Mathias"

print("0 Hello, my name is {:}".format(name))
print()
print("1 Hello, my name is {:10}. Nice to meet you".format(name))
# to left align it
print("2 Hello, my name is {:<10}. Nice to me
et you".format(name))
# to right align
print("3 Hello, my name is {:>10}. Nice to meet you".format(name))
# to center it
print("4 Hello, my name is {:^10}. Nice to meet you".format(name))

# we can also add positional or keyword arguments to this
# positional
#print("5 Hello, my name is {0:10}. Nice to meet you".format(name))
# keyword
#print("Hello, my name is {name:10}. Nice to meet you".format(name))