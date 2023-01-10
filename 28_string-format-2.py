# str.format() = 	optional method that gives users
#					more control when displaying output

# {} 	= 	format field

number = 3.14159

# let's say we only want to display the first two digits after the decimal
print("The number pi is {:.2f}".format(number))
# 3 digits - it also rounds so keep that in mind
print("The number pi is {:.3f}".format(number))


num = 1000

# we want to add commas at the thousands place
print("The number is {:,}".format(num))

# we can display our number as a binary
print("The number is {:b}".format(num))

# octal
print("The number is {:o}".format(num))

# hexadecimal - lowercase x for lowercase 
print("The number is {:x}".format(num))
# hexadecimal - uppercase X for uppercase 
print("The number is {:X}".format(num))

# scientific notation - same lowercase to lower upper to upper
print("The number is {:e}".format(num))
print("The number is {:E}".format(num))