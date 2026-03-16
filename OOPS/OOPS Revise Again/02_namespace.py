class Chai:
    orgin = "India" 

print(Chai.orgin)

Chai.is_hot = True #object

print(Chai.is_hot)

#creating objects from class Chai
masala = Chai()
print(f"Masala : {masala.orgin}") # Masala : India
print(f"Masala :{masala.is_hot}") # Masala :True

masala.is_hot = False # Hey we are changing here Ok 
# Let's see what happen if you change in iside of object. 
# should this change be propagated inside the class as well? 

print("Class :", Chai.is_hot) # Class : True
print(f"Masala :{masala.is_hot}") # Masala :False 

# so each object having its own namespace which doesn't affect other objects. 
# Also doesn't effect class as well. 
# By default, if you wish you can but by default you can go ahead and add more values to it.

masala.flavor = "Masala"
print("Flavour :", masala.flavor) # Flavour : Masala