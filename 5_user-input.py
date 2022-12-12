#Basicly all input is a string, if we want to make maths with it we need to cast it.
#if we casted an input datata, and we want to print it we need to cast it back to str

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = input("How tall are you?: ")

#age = age + 1

print("Hello "+name)
print("You are "+str(age)+" years old.")
print("You are "+str(height)+" cm tall")