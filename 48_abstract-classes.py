# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a DECLARATION but does not have an IMPLEMENTATION

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class
# inherited abstract methods MUST BE OVERRIDED!!!


# abstract classes are like templates

# we have to import the abc - abstract based class
from abc import ABC, abstractmethod

# we have to pass ABC as argument to the abstract class
class Vehicle(ABC):
    # and have to add the abstractmethod decorator to over the methods

    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    # if we don't implement the  
    def go(self):
        print("You drive the car")
        
    def stop(Self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")

    def stop(Self):
        print("This car is stopped")
        
# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()

    