# Yo are creating a tea menu board. Each items must be numbered.
# Task: Use enumerate() to print meny item with numbers

# Example of enumerate():
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# s = list(enumerate(seasons))
# print(s) #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# s2 = list(enumerate(seasons, start = 1))
#  print(s2) #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start = 1):
    print(f"{idx} : {item} chai")