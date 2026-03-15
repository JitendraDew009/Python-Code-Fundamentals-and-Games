# ==============================================
chai_types = ["Light", "Kadak", "Ginger", "Kadak"]

strong_chai = list(filter(lambda chai: chai == "Kadak", chai_types))

print(strong_chai)

# ================================================
# filter() : used to select the elements from the iterable based on the function.
# syntax : filter(function, iterable)

profit = [100,-50, 270, -200, 300, 120]

# filter profit values less than zero

loss = list(filter(lambda p : p < 0, profit)) #you need to convert to list or tuple dtype to see the result
print(loss)

# ================================================================
# create a list of word and filter words with length>5 

words = ['apple', 'jammy', 'laptop', 'samsung']
length = list(filter(lambda x: len(x)>5, words ))
print(length)
