# lists = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spagetti"]

print(food)
print(food[3])

food[3]="sushi"
print(food[3])
print("----------")

food.append("ice cream")
food.remove("hotdog")
food.insert(0, "cake")
food.insert(0, "zuccini")
# pop removes the last element of the list
food.pop()
# sort sorts the list alphabeticly
food.sort()

for i in food:
    print(i)
    
print("----------")
# clear removes all elements from the list
food.clear()
if len(food) == 0:
    print("it's empty bruw")
print(food)
    