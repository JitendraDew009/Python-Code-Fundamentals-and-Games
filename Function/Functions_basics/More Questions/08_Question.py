# Function with **kwargs
# calculate a function that accepts any number of keyword arguments and prints them in the format.
# key:value

def print_kwargs(name, power):
    print("Name ", name, "Power ", power)

print_kwargs(name = "Ironman", power = "Jet fly") # Name  Ironman Power  Jet fly
print_kwargs(power = "Jet fly", name = "Ironman") # Name  Ironman Power  Jet fly
# print_kwargs(name = "Ironman") # TypeError: print_kwargs() missing 1 required positional argument: 'power'

print("//////////NOW USE ** kwargs////////////////")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}") #formating string

    
print_kwargs(name = "Ironman", power = "Jet fly") # name : Ironman 
                                                 # power : Jet fly
print("------------------")
print_kwargs(power = "Jet fly", name = "Iroman") # power : Jet fly
                                                 # name : Ironman 
print("------------------")
print_kwargs(name = "Iroman") # name : Ironman