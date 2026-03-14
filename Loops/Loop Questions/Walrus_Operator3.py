flavours = ['masala', 'ginger', 'lemon', 'mint']
print(f"Available flavours: ", flavours)

while (flavour := input("Choose your flavour here : ")) not in flavours:
    print(f"Sorry, {flavours} is not available")

print(f"You chose {flavour} chai")