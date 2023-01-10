import random
# these are not "true random" numbers, they are "pseudo random"

# this gives us a random int between 1 and 6
x = random.randint(1,6)
# this gives us a random floating number between 0 and 1
y = random.random()

print(y)

# we can also generate a random pick from a list or other collection
# let's say we playing rock paper scissors
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

# let's say we're working with a deck of card
# we can shuffle them
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)