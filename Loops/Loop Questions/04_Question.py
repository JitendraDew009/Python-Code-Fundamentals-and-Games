# Reverse a String
# Pronlem: Reverse a string using a lopp
string = "Laptop"
reverse_string = "" 
for char in string:
    reverse_string = char + reverse_string
    print(reverse_string)
    # Output is
    # L
    # aL
    # paL
    # tpaL
    # otpaL
    # potpaL

print("-------------------------")
# But if I coreect the indentation of print.
string = "Laptop"
reverse_string = "" 
for char in string:
    reverse_string = char + reverse_string
print(reverse_string)