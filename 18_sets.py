# set = a collection which is unordered, unindexed. No duplicate values allowed
# set is faster then list
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")
utensils.remove("fork")
dishes.update(utensils)
#utensils.clear()
dinner_table = utensils.union(dishes)

for i in dishes:
    print(i+" ",end="")
print()  
    
for i in utensils:
    print(i+" ",end="")
print()
print("------")

# to print the elements that occur only in one set
print("difference: ")
print(dishes.difference(utensils))
# to print the similar ones
print("intersection: ")
print(utensils.intersection(dishes))