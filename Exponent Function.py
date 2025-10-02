#print(2**3) # ans is 8 (2^3)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range (pow_num): # pow_num yaha 1 se chalu hoga because we have already given the index for result is 1
        result = result * base_num
    return result
    
print(raise_to_power(3,3)) # 27
print(raise_to_power(3,4)) # 27
print(raise_to_power(3,5)) # 27
print(raise_to_power(3,6)) # 27
