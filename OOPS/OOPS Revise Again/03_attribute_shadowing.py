class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai() # this is object we created
print(cutting.temperature) # hot

cutting.temperature = "Mild"

print(f"After changing : {cutting.temperature}") # After changing : Mild
print(f"Direct look into the class : {Chai.temperature}") # Direct look into the class : hot

# see after changing the value of temperature of object "cutting" it changes.(Mild)
# But if you see the direct reference of class of temperature is hot by Default.

# Now lets delete the cutting.temperature
del cutting.temperature
print("After changed and delete we get old one that was :",cutting.temperature) 
# After changed and delete we get old one that was : hot   

# ok now one more experiemnt
cutting.cup = "small"
print("Cup size is: ", cutting.cup) # Cup size is:  small

del cutting.cup
print("Cup size is: ", cutting.cup) # AttributeError: 'Chai' object has no attribute 'cup'

# ya!, you injected the attribute and then deleted the attribute so there is no fallback like cutting.temperature has which was "hot".
# That's why showed attribute error because there was no fall back of cutting.cup