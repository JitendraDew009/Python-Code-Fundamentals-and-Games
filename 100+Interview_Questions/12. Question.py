# 12. Adding Two list element together
list1 = [1,2,3]
list2 = [4,5,6]
newlist = []
# newlist = list1 + list2 
# print(newlist) [1, 2, 3, 4, 5, 6]
for i in range(0, len(list1)):
    newlist.append(list1[i]+ list2[i])
print(newlist)

