# ye ek cotainer hai jaha various value store kar sakte hain
# ye ek list ke samaan hota hain
coordinates = (4,5,6,7,8,9)
# coordinates[1] = 10 #tuple ko change ya modefiy nahi kiya ja sakta = immutable, what u see is what you get

print(coordinates[1])
coordinates = [(4,5), (6,7), (80,34)]
# ann ye ek list ke ander tuple hain now this chunks of tuple can be change.
coordinates[1] = (5,5)
print(coordinates)