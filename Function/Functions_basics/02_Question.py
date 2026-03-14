# Print element of a list in single line

cities = ["bangalore", "raipur", "mumbai", "bhopal", "nagpur", "gurgoan", "chennai", "bilaspur", "delhi" ]

def print_list(lst):
    for item in lst:
        print(lst, end=" ") # lst 

print_list(cities)

print("\n")

print("--------------Can you SEE the deifference----\n")

cities = ["bangalore", "raipur", "mumbai", "bhopal", "nagpur", "gurgoan", "chennai", "bilaspur", "delhi"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print()