# Fruit Ripeness Checker
# Problem: Determined if a fruit is ripe, overripe, or unripe based on its color.(e.g Banana : Green - Unripe, Yellow - Ripe , Brown - Overripe)

# This solution is attempt honestly but limitation of this solution is that I have created for all kind of fruits. 
# if chikoo color is brown that mean overripe not at all... 
# so it is already given in question for banana. so make it for banana. Right? so, code again. 
# ------------------------------------------------------------------------------------------------------------
# color = input(
#     "Fruit Ripeness Checker " \
#     "Choose Your Fruit Color " \
#     "A. Green " \
#     "B. Yellow " \
#     "C. Brown :"  
# )

# if color == "A":
#     print("Your fruit is Unripe ")
# elif color == "B":
#     print("Your fruit is Ripe")
# elif color == "C":
#     print("Your fruit is Overripe")
# else:
#     print("Invalid Answer")
# ------------------------------------------------------------------------------------------------

# here is new code and new attempt

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Over Ripe")
            