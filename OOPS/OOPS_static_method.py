# Static Methods that don't use self parameter (work at class level)

# Decorator allow us to wrap another function in order to extendthe behaviour of the wrapped function, without permanently modefying it.

class Student:
    @staticmethod #decorator
    def college():
        print("GGU College")
s1 = Student()
print(s1.college())  