# Define a Employee class with attributes role, department & salary. This class also a showDetail() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetail(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee): #engg # inherit the property of Employee

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "Rs.75,000") #   inherit the property of Employee


e1 = Employee("accountant", "Finance", "Rs.60,000")
print("/-------------------------/")
e1.showDetail()

print("/////////////////")
engg1 = Engineer("Elon Musk", 49)
print("/-------------------------/")
engg1.showDetail()
        