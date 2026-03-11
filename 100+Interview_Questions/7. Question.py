# 7. Writing a FIBONACCI Series
fib = [0, 1]       # Starting list with the first two Fibonacci numbers
n = 5              # Number of additional Fibonacci numbers to generate

for i in range(n):                 # Loop runs 5 times (i = 0 to 4)
    fib.append(fib[-1] + fib[-2])  # Add the sum of last two elements to the list

# Initial list: [0, 1]

# Iteration 1: 1 + 0 = 1 → [0, 1, 1]

# Iteration 2: 1 + 1 = 2 → [0, 1, 1, 2]

# Iteration 3: 2 + 1 = 3 → [0, 1, 1, 2, 3]

# Iteration 4: 3 + 2 = 5 → [0, 1, 1, 2, 3, 5]

# Iteration 5: 5 + 3 = 8 → [0, 1, 1, 2, 3, 5, 8]

print(', '.join(str(e) for e in fib))  # Convert each number to string and join with commas
