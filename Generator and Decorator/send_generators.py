def chai_customer():
    print("Welcome! What chai would you like ?")

    order = yield
    while True:
        print(f"Preparing : {order}")
        order = yield # work as stopper otherwise this code will go on infite run.

stall = chai_customer()
next(stall)

stall.send("Masala chai")
stall.send("Lemon chai")
stall.send("Black chai")