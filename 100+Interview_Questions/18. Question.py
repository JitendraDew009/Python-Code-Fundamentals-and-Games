# 18. Removing all whitespaces in a string.
string = 'C O D E'
string2 = string.replace( " ", "")
print(string2) #CODE

#Another apprach with join
string3 = "".join(char for char in string if char != " ")
print(string3)

#Another approach with regular expression 

import re
str1 = "A B C D"
spaces = re.compile(r'\s+')
result = re.sub(spaces, "", str1)
print(result)
