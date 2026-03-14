# return keyword fuction se jaankari waspi karni ki anumati de sakta hain.
def cube(num):
    num*num*num

print(cube(3)) # none print hota hai to ans kyon ki vo execute nahi ho raha.

def cube(num):
   return num*num*num
print(cube(3))