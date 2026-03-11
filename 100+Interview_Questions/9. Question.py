# Finding the minimum number in a list.
number_list = [100,5,8,9,-1,55,66,744,45,69,8523,1,0]

min_value = number_list[0]

for num in number_list:
    if min_value > num:
        min_value = num #If it finds a number smaller than the current min_value, it updates min_value.
print(min_value)

# or we can use built in function (min).
print(min(number_list))