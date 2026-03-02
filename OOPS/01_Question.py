# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create method tp print the average

class Student():
    # name = "Jitendra"
    # marks = [99,80,97]
    def __init__(self, fullname,marks):
        self.fullname = fullname
        self.marks = marks
    
    def average_calc(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Hi!,",  self.fullname  ,"your average score is:",sum/3 )    
s1 = Student("Jitendra Dewangan", [99,80,97])

s1.average_calc() #Hi ! Jitendra Dewangan your average score is:  92.0

s1.fullname = "Daleshwar"
s1.average_calc()