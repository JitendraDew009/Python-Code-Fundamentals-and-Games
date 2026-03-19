import random

# Generate a random float between 0.0 and 1.0
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Generate a random float between 5 and 10
random_uniform = random.uniform(5, 10)
print(f"Random float between 5 and 10: {random_uniform}")