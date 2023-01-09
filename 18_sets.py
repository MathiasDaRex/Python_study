# set = collection which is unordered, unindexed. No duplicate values
tools = {"hammer","screwdriver","knife","scissors"}
files = {"small file","medizum file","rasp","scissors"}

# tools don't necessary appear in the order that they declared
# AND THAT'S WHY IT'S FASTER THAN A LIST

# add an element:
#tools.add("drill")

# remove a element
#tools.remove("knife")

# clear the whole set
#tools.clear()

# add all elements from one set to another (files to tools right now)
# tools.update(files)

# we can also join two sets together and create an entirely new set
#tool_trolley = tools.union(files)

#for i in tool_trolley:
#    print(i)
    
print("-----")
# we can also check the similarities and the differences
# between the elements of two sets

# check what elements does tools have, that files doesn't
print(tools.difference(files))
# and the opposite:
print(files.difference(tools))

# check the common items of two sets, returns with the common values
print(tools.intersection(files))
