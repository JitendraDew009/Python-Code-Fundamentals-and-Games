# Reducing Code Duplication
# you are managing a busy tea stall.
# you recive any orders and want to print each customer's name along with the type of chai they ordered.
# Task: - Write function print_order(name, chai_type)
    #   - call it multiple times for different customers.

def print_order(name, chai_type): #name, chai_type are parameters
    print(f"{name} ordered {chai_type} chai!")


print_order("Aman", "Masala") # "Aman", "Masala" are arguments
print_order("Balu", "Lemon")
print_order("Cinu", "Oolong")
print_order("Digi", "Herbal")
