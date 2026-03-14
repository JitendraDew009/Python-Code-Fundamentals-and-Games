# Print all element in a list by using recursion.
# hint: use list & index as parameters
def print_lsit(list, idx=0):
    if (idx == len(list)):
        return 
    print(list[idx], end =' ') # with end = " " 
    print_lsit(list, idx+1)
fruit = ["mango", "apple", "grapes", "orange"]

print_lsit(fruit)

print("\n-------------------------------")
def print_lsit(list, idx=0):
    if (idx == len(list)):
        return 
    print(list[idx]) #without end = " "
    print_lsit(list, idx+1)
fruit = ["mango", "apple", "grapes", "orange"]

print_lsit(fruit)