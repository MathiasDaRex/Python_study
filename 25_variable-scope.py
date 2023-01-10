# scope = 	The region that a variable is recognized
#			a variable is only available from inside the region it is created
#			a global and locally scoped versions of a variable can be created

name = "Mathias" # global scope (available inside & outside functions)

def display_name():
#	if we remove the local version, it's gonna call the global variable
    name = "Rex" # local scope (available only inside this function)
    print(name)
    
display_name() 	# local
print(name)		# global

# HIERARCHY
#	L = Local
#	E = Enclosing
#	G = Global
#	B = Built-in
