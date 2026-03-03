# When one class (child/derevied) drives the properties & methods of another class (parent/base).

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
print(car1.color)
print(car1.start()) #See we inheritated properties from Car into Toyo Car. 
# that's why car1.start() is working