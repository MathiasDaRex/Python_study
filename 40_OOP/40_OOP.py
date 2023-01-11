# if you are sitting at your table, you are sorrounded by objects
# like your keyboard, mouse, monitor, and your computer
# but it can be a cup of tea, your snacks, basicly anything from real world
# objects are meant to be mimic real world objects by assigning a combination of attributes
# attributes like - name, age, height, purpose, color, ect...
# and they also have methods, which are responsible for actions
# like you eat, sleep, study, go biking, anything

# to create an object we have to create a class. a class cak act as a blueprint
# that will describe what attributes and methods that our object will have.
# we can create classes in a separate file, or within the main module.
from car import Car
 
car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford","Mustang",2022,"red")
 
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()