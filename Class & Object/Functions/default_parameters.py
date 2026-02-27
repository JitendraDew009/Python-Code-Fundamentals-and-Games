# Example  of Default parameters 
def cal_prod(a=1, b=5):
    print(a * b)
    return a * b
cal_prod() # 1 * 5 = 5

print("---Another Example of Default parameters--- ")

# Another 2nd Example of Default parameters 
def cal_prod(a, b=5): # a is variable and b is constant "first = non default argument then last default argument" <-- this is correct pattern
    print(a * b)
    return a * b
cal_prod(1) # 1 * 5 = 5
cal_prod(2) # 2 * 5 = 5
cal_prod(3) # 3 * 5 = 5
cal_prod(4) # 4 * 5 = 5

print("---Another 3rd Example of Default parameters--- ")

# Another Example of Default parameters // Arguments like (a=5, b) THIS WILL THROW YOU AN ERROR BECAUSE  (a = 5 which is default arguement and b = non default argument)
def cal_prod(b, a= 5): #fix this (b, a=5) instead of (a=5, b)
    print(a * b)
    return a * b
cal_prod(1) # ERROR // after fix, you will get 5
