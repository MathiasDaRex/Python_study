# dictionary = 	A changeable, unordered collection of unique key:value pairs
# 				Fast because they use hashing, allow us to access a value quickly

# Let's create a dictionary with countries and their capitals

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Bejing",
            "Russia":"Moscow"}
# to access records, we have to use the key, not indexes
print(capitals['Russia'])
# that is not safe, because if the key doesn't exists, it thows an error.
# print(capitals['Germany'])

# But if we use the get method, it's returning with 'None'
print(capitals.get("Germany"))

# if we want to acces all keys
print(capitals.keys())

# also only values:
print(capitals.values())

# or everything:
print(capitals.items())

# another way of displaying everything with a for loop:
#for key,value in capitals.items():
#    print(key, value)

# dictionaries are mutable - we can change if the program already running
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
# to remove a key-value pair:
capitals.pop("Russia")
# to remove everything:
capitals.clear()

print("----")
for key,value in capitals.items():
    print(key, value)
print("----")