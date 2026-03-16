# Everything in python is object. even this class is an object internally 

class A1:
    pass

class B1:
    pass

print(type(A1)) #<class 'type'>


store = A1()

print(type(store)) # <class '__main__.A1'>
print(type(store) is A1) # True
print(type(store) is B1) # False

