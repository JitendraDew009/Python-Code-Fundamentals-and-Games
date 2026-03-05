# Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2): # the special method __gt__ (greater than), which compares the price of two Order objects.

        return self.price > ord2.price


ord1 = Order("Lays", 10)
ord2 = Order("Fruits", 60)     
print(ord1 > ord2) #False
print(ord1 < ord2) #True
# When you run print(ord1 > ord2), Python calls ord1.__gt__(ord2).
# That evaluates 10 > 60, which is False

