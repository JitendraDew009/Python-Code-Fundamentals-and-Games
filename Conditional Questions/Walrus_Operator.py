# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# Walrus Operator ( := )

# Thiis is shorter version of above programme
value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
    