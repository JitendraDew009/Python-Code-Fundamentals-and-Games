# Password Checker
# Problem : check if a password is 'weak', 'Medium' or 'strong'. Criteria < 6 chars (weak), 6-10 chars (Medium) and >10 chars (strong).
password = "Secure3p@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your Password Strength is",strength)