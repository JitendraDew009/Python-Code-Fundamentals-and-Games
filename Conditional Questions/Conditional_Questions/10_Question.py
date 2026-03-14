# Pet food recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g Dog: <2years - Puppy food, Cat:> 5years - Senior cat food).

pet = "Cat"
pet_age = 12

if pet == "Dog" and pet_age < 2:
    print("Puppy Food")
elif pet == "Dog" and pet_age >=2:
    print("Adult Dog food")
elif pet == "Cat" and pet_age > 5:
    print("Senior Cat food") 
else:
    print("Junior Cat Food")   