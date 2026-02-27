# Write a recursive function to calculate the sum of the first n natural numbers.

def number(n):
    if n == 0:
        return 0
    return number(n-1) + n

sum = number(5)

print(sum)


# How It Works
# - Base Case
# - If n == 0, the function returns 0.
# - This stops the recursion from going infinitely.
# - Recursive Case
# - Otherwise, it calls number(n-1) and adds n.
# - This keeps reducing the problem until it reaches the base case.

# Step-by-Step Trace for number(5)
# - number(5) → number(4) + 5
# - number(4) → number(3) + 4
# - number(3) → number(2) + 3
# - number(2) → number(1) + 2
# - number(1) → number(0) + 1
# - number(0) → 0 (base case)
# Now we add back up:
# - number(1) = 0 + 1 = 1
# - number(2) = 1 + 2 = 3
# - number(3) = 3 + 3 = 6
# - number(4) = 6 + 4 = 10
# - number(5) = 10 + 5 = 15

# \mathrm{Sum\  of\  first\  n\  natural\  numbers}=\frac{n(n+1)}{2}

