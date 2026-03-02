# Methods are function that belong to objects.
class Student:
    college_name = "GGU College" #class attribute, which is comman for whole
   
    name = "anonymous" #class attributes

    def __init__(self, fullname, marks): #constructor always takes argument a self parameter. So self is necessary to write in () then you add more parameters
        self.name = fullname #self is reference of object, self.name means object ke liye name define karna  
        
        self.marks = marks #object attribute > class attribute
 #Inside of class, functions are there called Method 
    #Method creation 1  
    def welcome(): #this will show you a Type Error
        print("Welcome Everyone")
    
    #Method creation 2
    def welcome(self): #this will not
        print("Welcome", self.name)  
    
    #Method creation 3
    def get_marks(self):
        return self.marks 

s1 = Student("Jitendra", 100)

s1.welcome() #Welcome Jitendra  #Method 2 call 

print(s1.get_marks()) # 100# #Method 3 call