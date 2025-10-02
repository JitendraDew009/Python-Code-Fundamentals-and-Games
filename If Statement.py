is_male = True

if is_male:
    print("You are a male") # True hai toh print hoga nahi toh nahi hoga.
else:
    print("You are not male")

print("------------------------------")
is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or taller or both") # True hai toh print hoga nahi toh nahi hoga.
else:
    print("You are neither male nor tall") # agar dono false honge toh hi print hoga

print("------------------------------")
is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a male or taller or both") # True hai toh print hoga nahi toh nahi hoga.
else:
    print("You are neither male nor tall") # agar dono false honge toh hi print hoga

print("------------------------------")
is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or taller or both") # True hai toh print hoga nahi toh nahi hoga.
else:
    print("You are neither male nor tall") # agar dono false honge toh hi print hoga

print("------------------------------")
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a male or taller or both") # True hai toh print hoga nahi toh nahi hoga.
elif is_male and not (is_tall):
    print("Yo are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are neither male nor tall") # agar dono false honge toh hi print hoga

#various data ke prati process karne me sahayta mil sake
