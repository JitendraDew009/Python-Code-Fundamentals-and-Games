# Movie tickets are priced based on age: $12 for adult(18 and over ), $8 for children. Everyone gets a $2 discount on wednusday

age = int(input("Provide me an age :"))
day = input("Is today Wednusday? Y/N :")

price = 12 if age >= 18 else 8

if day == "Y":
    price = price - 2

print("Your Ticket Price is $", price)