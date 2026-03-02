# Constructor -> All classes have a fuction called __init__() which is always executed when object is being initiated.

class Student:
    college_name = "GGU College" #class attribute, which is comman for whole
   
    name = "anonymous" #class attributes

    def __init__(self, fullname, marks): #constructor always takes argument a self parameter. So self is necessary to write in () then you add more parameters
        self.name = fullname #self is reference of object, self.name means object ke liye name define karna  
        
        self.marks = marks #object attribute > class attribute
        
        print("Adding new student in database..")
        
        print(self) #<__main__.Student object at 0x00000114B5CD7230> 


s1 = Student("Jitendra", 100)
s2 = Student("Jitu", 96)
print(s1) # s1 = self = <__main__.Student object at 0x00000114B5CD7230> 

print(s1.name) # Jitendra
print(s1.college_name) #GGU college
print(s1.name) # Output will be Jitendra not anonymous why? because of precedence object attribute > class attribute
print(s2.name,  s2.marks) 