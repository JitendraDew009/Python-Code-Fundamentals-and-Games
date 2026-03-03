class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shradha")
print(s1)
print(s1.name)
# del s1 # delete the object
print(s1) #ameError: name 's1' is not defined
s1 = Student("harish")
print(s1)
print(s1.name)