# Hiding the implementation detail of a class and only showing the essential features to the user.
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started...")

car1 = Car()
car1.start() # Car Started..., here you used on method to run a fuction. you are hiding the implementation.


    