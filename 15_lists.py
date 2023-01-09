# lists = store multiple items in a single variable

food = ["pizza","hamburger","hot-dog","spagetti","pudding"]

# change elements while runtime
food[0] = "sushi"

print(food[0])
print(food[2])
print(food[4])
# print(food[5]) index out of range exception

# add elements to the end of the list
food.append("ice cream")

# remove value
food.remove("hot-dog")

# remove last element
#food.pop()

# insert element to a given index
# here "cake" to the 0 index
food.insert(0, "cake")

# sort alphabetically
food.sort()

# fully clear the list
#food.clear()

print()
print("All: ")
print()
# show all elements
for x in food:
    print(x)

