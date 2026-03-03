class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("12345", "abcde")
print(acc1)
print(acc1.acc_no)
print(acc1.acc_pass)

# use __ (dobule underscore) to private the access

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #use __(double underscore to do private access)

    def reset_password(self):
        print(self.__acc_pass) # here you can print

acc1 = Account("12345", "abcde")
print(acc1)
print(acc1.acc_no)
# print(acc1.__acc_pass) #Look they show attribute error means access is under controled.
print(acc1.reset_password())

print("////////////Used __ to make private ////////////////////")
class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello")

    def welcome(self): # use to work on inside the class but never give access outside of the class because sometime all fuction are nested.
        self.__hello()

p1 = Person()

print(p1.welcome())