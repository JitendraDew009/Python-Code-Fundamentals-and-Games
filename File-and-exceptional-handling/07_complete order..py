class InvalidChaiError(Exception): 
    pass

def bill(flavor, cups):
    menu = {"masala" : 20, "ginger" : 40 }
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cup(s) of {flavor} chai: Rs.{total}")
    
    except Exception as e:
        print("Error :", e)
    finally:
        print("Thank You for visiting Our Shop!")
    
bill("masala", 2)
print("============")

bill("ginger", "two")
print("============")

bill("elaichi", 1)





