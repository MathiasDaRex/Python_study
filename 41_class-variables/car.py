class Car:
    
    # if we create variables inside the class but outside the constructor
    # every car object gonna have it.
    
    wheels = 4	# class variable
    
    # in Python we dont have constructors, instead we have init function
    def __init__(self, make, model, year, color):
        self.make = make 	# instance variable
        self.model = model	# instance variable
        self.year = year	# instance variable
        self.color = color	# instance variable