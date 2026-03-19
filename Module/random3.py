import random

def roll_dice():
    return random.randint(1, 6)

# Roll the dice 5 times
for i in range(6):
    print(f"Roll {i+1}: {roll_dice()}")

# roll_dice()

