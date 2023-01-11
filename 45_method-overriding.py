class Animal:
    def eat(self):
        print("This animal is eating")
        
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating")
    
class Cow(Animal):
    def eat(self):
        print("This cow is eating")

rabbit = Rabbit()
cow = Cow()
rabbit.eat()
cow.eat()