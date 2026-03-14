# Imporve readability
# You sell different chai sizes.
# Instead of writing formulas everywhere, create a function.
# task:
# write calculate_bill(cups, price_per_cup)
# return total bill
# use this function for multile orders

# def calculate_bill(cups, price_per_cup):
#     total_bill = cups * price_per_cup 
#     print(f"Your order was {cups} cup of tea which cost is Rs.{price_per_cup} per cup.")
#     print(f"Your total bill is Rs.{total_bill}")

# calculate_bill(3,15)

def calculate_bill(cups, price_per_cup):
    total_bill = cups * price_per_cup 
    print(f"Your order was {cups} cup of tea which cost is Rs.{price_per_cup} per cup.")
    print(f"Your total bill is Rs.{total_bill}")
    return total_bill #using return , it return the value to function so you have to print it or put after the print fuction. 

calculate_bill(3, 15)
# print(f"Total Bill for Table 2 : Rs.",calculate_bill(3,15))
