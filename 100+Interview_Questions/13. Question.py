# 13. Comparing two strings for ANAGRAMS

str1 = "Listen"
str2 = "Silent"

str1 = str1.replace("", "").upper()
str2 = str2.replace("", "").upper()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")



# print("------------------------------------")
# # Using colections.Counter

# from collections import Counter
# def is_anagram(s1, s2):

#     return Counter(s1.replace(" ", "").upper()) == Counter(s2.replace(" ", "").upper())

# is_anagram("Dormitory", "Dirty room")  # Returns True
# is_anagram("Hello", "Olelh")           # Returns True
# is_anagram("Python", "Java")           # Returns False

# # sorted(str1) turns "LISTEN" into ['E', 'I', 'L', 'N', 'S', 'T']

# # sorted(str2) turns "SILENT" into ['E', 'I', 'L', 'N', 'S', 'T']