# Loop control statements = change a loops execution from it's normal sequence

# break = 		used to terminate the loop entirely
# continue = 	skips to the next iteration of the loop
# pass =		does nothing, acts as a placeholder

# if we want to exit the loop at a specific condition we can use break
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break


# to skip an iteration we can use continue
# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")

# pass does nothing, acts as a placeholder
for i in range(1,21):
    
    if i == 13:
        pass
    else:
        print(i)