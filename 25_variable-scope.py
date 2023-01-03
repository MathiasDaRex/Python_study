# variable scope = 	the region that a variable is recognized
#					A variable is only available from inside the region it is created.
#					A global and locally scoped versions of a variable can be created
#						local scope - variable declared inside a function
#						global scope - variable declared outside a function, and can be used inside and outside, but only INSIDE the MODULE

name = "Mathias" 			# global variable with global scope (abailable inside & outside function)

def display_name():
    name = "Rex" 		# local variable with local scope (available only inside this function)
    print("hi",name)

# print(name)			we cannot access it from here.
print("HELO "+name)
display_name()