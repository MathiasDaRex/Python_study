# tuple = 	a collection which is ordered and unchangeable
#			used to group together related data

student = ("Mathias",21,"male")

print(student.count("Bro"))
print(student.index("male"))

for i in student:
    print(i)
print("------")

print(student[2])
print("------")
    
if "Mathias" in student:
    print("Mathias is here!")