# map() : used to apply a function to every element in the iterable/squence
# syntax : map(function, iterable)

num = [1000, 2000, 3000]

result = list(map(lambda x : x + 100, num)) #you need to convert to list or tuple dtype to see the result
print(result) # now we can print this result
