# 11. Coverting a list into a string
list = [ 'P', 'Y', 'T', 'H', 'O', 'N']
# This is better approach
string = "".join(list)
print(string)
print(type(string))

#This is not better apporach
# string = str(list)
# print(string) #['P', 'Y', 'T', 'H', 'O', 'N']
# print(type(string)) #<class 'str'>