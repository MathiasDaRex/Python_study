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

class Car:
    
    # in Python we dont have constructors, instead we have init function
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    
    def drive(self):
        print("This",self.model,"is driving")
        
    def stop(self):
        print("This",self.model,"is stopped")