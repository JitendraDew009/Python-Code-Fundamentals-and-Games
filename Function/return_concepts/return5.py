def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai is over"
        print("chaiout") # this will never wok after return, put above the return if you want to make it workable.
    print("Chai is available")

chai_status(0) # see even it satisfies the if conditon. so it executes return but after return there will be no execution.

chai_status(1) # this will never work out until you call it first.
