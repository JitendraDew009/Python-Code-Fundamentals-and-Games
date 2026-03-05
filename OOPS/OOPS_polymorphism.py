# Operator overlaoding = 1 operator has multiple forms
# print(1+2) #3

# print("GGU" + "MSTMG") #concatenate

# print([1,2,3]+[4,5,6]) #merge two list

# print(type([1,2,3])) #<class 'list'>

# //////////////////////////////////
            # Dunder functions
# a + b  a__and__(b)
# a - b  a__sub__(b)
# a * b  a__mul__(b)
# a / b  a__truediv___(b)
# a % b  a__mod____(b)

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")

#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(1, 3)
# num1.showNumber() # 1 i + 3 j

# num2 = Complex(4, 6)
# num2.showNumber() # 4 i + 6 j

# num3 = num1.add(num2)
# num3.showNumber() # 5 i + 9 j
# print(num1 + num2)
#So if we want print(num1 + num2) but we will get Type error. 

# So we use dunder function in such way like __add__

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1, 3)
num1.showNumber() # 1 i + 3 j

num2 = Complex(4, 6)
num2.showNumber() # 4 i + 6 j

num3 = num1 + num2

print("Add",num3.showNumber()) # 5 i + 9 j

num3 = num1 - num2
print("Sub",num3.showNumber()) # -3 i + -3 j
# print(num1 + num2) 

