# Search for a number x in this tuple using loop and print the index of x if found, else print "Not Found"
# nums = [1, 4, 9, 16, 26, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 26, 36, 49, 64, 81, 100, 36]
x = 36
idx = 0

# Simple one 
for i in nums:
    if (i == x):
          print(x,"is found at idx", idx)
        #   break # add if you want to break at first occurance
    idx += 1

# optimized one

# for i in nums:
#     if (i==x):
#         print(x,"is found at", idx)
#         idx += 1
#         break
#     else: idx += 1
# else:
#     print(x,"Not found")