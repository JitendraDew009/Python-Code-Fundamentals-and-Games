for i in nums:
    if (i==x):
        print(x,"is found at", idx)
        idx += 1
        break
    else: idx += 1
else:
        print(x,"Not found")