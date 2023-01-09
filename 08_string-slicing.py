# slicing =	create a substring by extracting elements from another string
#			indexing[] or slice()
#			[start:stop:step] - normally step is 1 by default

# indexing[]

name = "Mathias Rex"

# first_name = name[0:7]
first_name = name[:7]
# last_name = name[8:11]
last_name = name [8:]
# to display every second letter
#funky_name = name[0:11:2]
# if we use it like this, python will assume the start and stop to
# be at the beginning and the end of the string
funky_name = name[::2]
reversed_name = name[::-1] # we count backwards


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# Slice function
website = "http://google.com"
website2 = "http://wikipedia.com"

# 1 - create a slice object invoking the slice function
# here we using (start,stop,step) syntax
# with indexing we can count backwards, to isolate the .com end
slice = slice(7,-4)

print(website[slice])
print(website2[slice])