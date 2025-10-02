from Student import Student
student1 = Student("Jim", "Business", 2.1, False)
student2 = Student("Pim", "Business", 7.1, True)
print(student1.name) # Jim
print(student1.gpa) # 8.1
print(student2.major) # Business

print(student1.on_honor_roll())
print(student2.on_honor_roll())
