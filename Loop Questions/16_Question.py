# You want to skip those and stop entirely if someone requests a restricted flavour.
# Task : Skip if flavour is "Out of Stock"
#       Break if flavour is "Discontinued"

flavours = ['Ginger', 'Out of Stock', 'Discontinued','Lemon']

for flavour in flavours:
    if flavour == 'Out of Stock':
        continue #skip
    if flavour == 'Discontinued':
        break # break and go out of the loop.
    print(f"{flavour} item found") # this is loop block
    
print(f"{flavour} is found # Out of the loop")