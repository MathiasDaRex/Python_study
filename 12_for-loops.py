import time
# for loop = 	a statement that will execute it's block of code
#				a limited amount of times
#
#				while loop = unlimited
#				for loop = limited

# count to 10
# for i in range(10):
# 		print(i+1)

# we can use step here too
#for i in range (50,100+1, 2):
#    print(i)

# we can iterate anything thats iterable, including strings
#for i in "Mathias Rex":
#    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    # to wait 1 seconds
    time.sleep(1)
print("Happy new year")