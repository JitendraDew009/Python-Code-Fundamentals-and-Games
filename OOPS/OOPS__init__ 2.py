# Constructor -> All classes have a fuction called __init__() which is always executed when object is being initiated.

class Student:
    
    def __init__(self, fullname): #constructor always takes argument a self parameter. So self is necessary to write in () then you add more parameters
        self.name = fullname
        
        print("Adding new student in database..")
        
        print(self) #<__main__.Student object at 0x00000114B5CD7230> 


s1 = Student("Jitendra")

print(s1) # s1 = self = <__main__.Student object at 0x00000114B5CD7230> 

print(s1.name) # Jitendra