# Constructor -> All classes have a fuction called __init__() which is always executed when object is being initiated.

class Student:
    def __init__(self): # Default Constructors
                
        print("Adding new student in database..")

    # Parameterized Constructors
    def __init__(self, fullname, marks): #constructor always takes argument a self parameter. So self is necessary to write in () then you add more parameters
        self.name = fullname
        self.marks = marks
        print("Adding new student in database..")
        
        print(self) #<__main__.Student object at 0x00000114B5CD7230> 


s1 = Student("Jitendra", 100)

print(s1) # s1 = self = <__main__.Student object at 0x00000114B5CD7230> 

print(s1.name, s1.marks) # Jitendra 100

s2 = Student("Arjun", 99)
print(s2.name, s2.marks) # Arjun 99 