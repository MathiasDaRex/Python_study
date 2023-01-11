from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford","Mustang",2022,"red")

# each object will have their own copy of the wheels variable
# but we can set it to another value at each instance
car_1.wheels = 2

# we can also change the class variable, so every instances will have that value
Car.wheels = 6

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)
