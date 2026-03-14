# Multiple return

# def chai_report():
#     return 100, 20 # sold, remaining

# sold, remaining = chai_report()
# print("Sold: ", sold)
# print("Remaining: ", remaining)

# Sold:  100
# Remaining:  20

# now open return7.py for its new variation

def chai_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
