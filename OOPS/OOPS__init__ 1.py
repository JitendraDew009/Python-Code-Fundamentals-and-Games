# Constructor -> All classes have a fuction called __init__() which is always executed when object is being initiated.

class Student:
    name = "Jitendra"
    def __init__(self): #constructor takes argument a self parameter
        print("Adding new student in database..")
        print(self) #<__main__.Student object at 0x00000114B5CD7230> 


s1 = Student()
print(s1) # s1 = self = <__main__.Student object at 0x00000114B5CD7230> 