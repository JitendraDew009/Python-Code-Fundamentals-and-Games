menu = [
    "Masala chai",
    "Iced Lmeon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]
#     [expression for item in iterable if condition]
iced_tea = [ tea for tea in menu if "Iced" in tea]
# or
iced_tea = [ my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)