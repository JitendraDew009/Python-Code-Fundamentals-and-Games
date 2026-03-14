x = 99
def func():
    x = 12
    return x
print (x) #99
print(func()) #12

print("///////////----**----////////////")

x = 100
def func3():
    global x
    x = 12 # if we remove this, it will take x = 100 which is global
    return x
print(x) #100
print(func3()) #12 ; # 100 by removing x = 12

print("///////////----**----////////////")
x= 101
def f1():
    global x
    x = 88
    def f2():
        print(x)
    f2()
f1() # 88 ; 101 if we don't remove x = 88 

print("///////**CLOSURE EXAMPLE**//////")
def sqaure(num):
    def actual(x):
        return x ** num
    return actual

f = sqaure(2)
g = sqaure(3)

print(f) #figure out how variables (f,g) are connect to ref. in memory 
print(g)

print(f(4)) #4 ** 2 = 16
print(f(3)) #3 ** 2 = 9
print(g(3)) #3 ** 3 = 27