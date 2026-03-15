def pure_func(cups):
    return cups * 10

total_function = 0

#this is not recommanded
def impure_func(cups):
    global total_function
    total_function += cups
