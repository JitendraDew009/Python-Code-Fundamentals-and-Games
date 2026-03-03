class Car:
    
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("fortuner", "Diesel")
car2 = ToyotaCar("prius", "electric")
print(car1.name)
print(car1.start())
print(car1.stop())