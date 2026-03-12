# Counting Digits, Letters, and Spaces in a String.

import re

str1 = "My phone number is 7852488544458"
cnt_number = re.sub("[^0-9]", "", str1)
cnt_letter = re.sub("[^a-zA-Z]", "", str1)
cnt_space = re.findall("[ \s]", str1)
print(len(cnt_space))
print(len(cnt_letter))
print(len(cnt_number))

#Just brain stroming....
# print(cnt_space)
# print(cnt_letter)
# print(cnt_number)

# number = " ".join(cnt_number)
# print(number)