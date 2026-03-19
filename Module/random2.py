
import random

# List of items
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Select a random fruit from the list
random_fruit = random.choice(fruits)
print(f"Randomly selected fruit: {random_fruit}")

# Shuffle the list of fruits
random.shuffle(fruits)
print(f"Shuffled list of fruits: {fruits}")

# Select 2 unique random fruits from the list
random_sample = random.sample(fruits, 2)
print(f"Random sample of 2 fruits: {random_sample}")