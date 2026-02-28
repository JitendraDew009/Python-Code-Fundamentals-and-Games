# Fuction with *args
# Write a fuction that takes variable number of arguemnts and returns their sum.
print("//////////////////////////////////")
print("////////with *args / *(any parameter) = can take multiple arguemnts//////////")

def sum_all(*args):  #with *args / *(any parameter) = can take multiple arguemnts
    return sum(args)

print(sum_all(1,5,8)) #14
print(sum_all(8,2,9,8,8,8,9,10)) #62

print("//////////////////////////////////")
print("/////////without *args / *(any parameter) = cannot take multiple arguemnts ( THROW YOU AN ERROR )/////////////")
def sum_all(*args):  #without *args / *(any parameter) = cannot take multiple arguemnts
    return sum(args)

print(sum_all(1,5,8)) #14


print("//////////////////////////////////")
print("//////////#IF WE ADD print(args)//////////")

def sum_all(*args):  #with *args / *(any parameter) = can take multiple arguemnts
    print(args) #IF WE ADD print(args)
    return sum(args)

print(sum_all(1,5,8)) 
# (1, 5, 8)
#14

print("//////////////////////")
print("//////////WE CAN DO OPERATIONS WITH ARGUMENTS BY USING *args////////////")
def sum_all(*args):  #with *args / *(any parameter) = can take multiple arguemnts
    print(args)
    for i in args:
        print(i * 2) #can do operations
    return sum(args)

print(sum_all(1,5,8)) 
# (1, 5, 8)
#2
# 10
# 16
# 14 (1+5+8)
print("//////////////////")
print("/////////not only *args but *jitendra (any parameter will work with *)/////////")
def sum_all(*jitendra):  #with *args / *(any parameter) = can take multiple arguemnts
    return sum(jitendra) #if you sum_all(jitendra) will create infinte reccursion.

print(sum_all(1,5,8)) #14
print(sum_all(8,2,9,8,8,8,9,10)) #62

print("//////////////////")