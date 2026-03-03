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

acc1 = Account("12345", "abcde")
print(acc1)
print(acc1.acc_no)
print(acc1.__acc_pass) #Look they show attribute error means access is under controled.