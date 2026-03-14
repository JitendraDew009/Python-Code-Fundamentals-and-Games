def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type # when you use it now it is making it chai_type nonlocal
        chai_type = "Kesar"

    kitchen()
    print("After kitchen update", chai_type) # without non local = After kitchen update Elaichi 
                        # with non local = After kitchen update Kesar 

update_order()

# If you want to access just above the inner fuction nonlocal is your friend.
# global is access to global object from anywhere