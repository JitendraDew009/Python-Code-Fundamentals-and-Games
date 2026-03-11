# 8. finding the maximum number of a list
number_list = [12, 3, 55, 23, 6 , 78 , 33 , 4]
max = number_list[0]

for num in number_list:
    if max < num:
        max = num # object ref shifting
print(max)