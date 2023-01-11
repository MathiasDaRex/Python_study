# classes can inherit attributes and methods from it's parent class
# it's like a parent-child relationship, where the child recives everything
# that the parent class has
class Animal:
    
    alive = True
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")
        
# to make rabbit a child class of animal,
# we have to pass Animal as an attribute to the class

# each child class can have their own unique methods and attributes
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()