f = open("D:\All Coding Stuff\Python Code\FreeCodeCamp\Python-Code-Fundamentals-and-Games\File Input\Output\demo.txt", "r")
# f = open("demo.txt", "r")
# data = f.read() # I am Jitendra Dewangan and 
                    # Learning foundation of Python
# data2 = f.read(10)
# print(data)
# print(data2) # I am Jiten
# print(type(data))
# print(type(data2)) # 0<class 'str'

line = f.readline() #To read single line of file. 
print(line) # I am Jitendra Dewangan and 
            # __________________________ (In result, Empty line will appear in result because I am Jitendra Dewangan and \n(next line) is there which is not appear.

line2 = f.readline() # Learning foundation of Python 
print(line2) 

# this f.readline will not work if you aleady read whole line
# data = f.read()
# print(data) I am Jitendra Dewangan and 
                    # Learning foundation of Python
# But after apllying it if run line1 and line2 thenm simulatenously then result will be empty.
#  line3 = f.readline() #you wil get empty next line
f.close()