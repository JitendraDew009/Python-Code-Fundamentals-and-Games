# intitialize = __init__  (initiate)

class ChaiOrder:
    def __init__(self, type_, size): #constructor
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary()) # 200ml of Masala chai

order_2 = ChaiOrder("Ginger", 220)
print(order_2.summary()) # 220ml of Ginger chai

# This is all getting constructors and INIT object or INIT values in the world of python.
