def process_order(item, quantity):
    try:
        price = {"masala" : 20}[item]
        cost = int(price) * int(quantity)
        print(f"totalcost is {cost}")
    
    except KeyError:
        print("Sorry that chai is not on menu")
    except ValueError:
        print("Quantity must be in number")

process_order("masala", 2) # totalcost is 40
process_order("masala", "two") # Quantity must be in number

