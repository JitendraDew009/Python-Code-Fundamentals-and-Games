# We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):

                                
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(85,87,98)
print(s1.percentage)
s1.phy = 98
print(s1.phy)
print(s1.calcPercentage) #but percentage is not upadting so

print("# ---------------------------------------------------")
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    @property #use it see the the magic or without it
    def Percentage(self):
                               
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(85,87,98)
print(s1.percentage)
s1.phy = 78
print(s1.Percentage) 
