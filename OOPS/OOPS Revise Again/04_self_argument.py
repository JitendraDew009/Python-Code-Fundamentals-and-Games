class Chaicup:
    size = 150 #ml

    def describe(self): # it is a function technically but we call it "Method" to be technically correct because it is inside the class.
                # self is representing to the class right now   
        return f"A {self.size}ml of chai cup"
    
cup = Chaicup()

print(cup.describe()) # A 150ml of chai cup

#print(Chaicup.describe()) # Error : Chaicup.describe() missing 1 required positional argument: 'self'. 

# It is referencing to the class object right now.

print(Chaicup.describe(cup)) # A 150ml of chai cup

cup_2 = Chaicup() # second object we created.

cup_2.size = 100 # New Attribute for size of cup_2 object
print(Chaicup.describe(cup_2)) # A 100ml of chai cup

# Go to class Chaicup then call method describe then give cup_2 object to work  