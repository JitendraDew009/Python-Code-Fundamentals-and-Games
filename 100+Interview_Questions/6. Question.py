# Counting the number of occurances of a character in a string


# string = ['G', 'o', 'o','g','l', 'e']
# print(string.count('o'))
# print(type(string))
# this solution is wrong because you have used list datatype not string as asked in question
# 
# So right solution is down below
# 
word = "Programming"
character = 'g'
count = 0
for letters in word:
    if letters == character:
        count += 1
print(count)