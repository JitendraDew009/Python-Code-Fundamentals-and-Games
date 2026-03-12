# 17. Counting special character in a string
# ----------------PROBLEM WITH APPROACH IS YOU CANNOT AND [] BECAUSE THERE IS NO ALTERNATIVE JUST LIKE QUOTE HAS ('',"","""" """",''' ''')--------------------
# import re

# sp_char = input("Let me count special character. Ok Write something :") #"!@#$%^&*()_+<>?:|"
# # cnt_sp_char = re.sub(r"[^!@#$%^&*()_+|;',.*-~`]", "", sp_char)
# cnt_sp_char = re.sub(r"[^!@#$%^&*()[_+<>?:|;',.*\-~`]", "", sp_char) 
# print(len(cnt_sp_char)) #17

#-------------------SO YOU SET instead of sting because it stores unique value------------------------------

specials = set("!@#$%^&*()_[]+<>?:|;',.*-~`")
sp_char = input("Write something: ")

count = sum(1 for ch in sp_char if ch in specials)
count = sum(1 for ch in sp_char if ch in specials)
count = sum(1 for ch in sp_char if ch in specials)
count = sum(1 for ch in sp_char if ch in specials)
print(count)
