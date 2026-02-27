# Recursion in Python (or any programming language) means a function calls itself to solve a problem. It’s often used when a problem can be broken down into smaller, similar subproblems.

# A recursive function has two parts:
# - Base case → the condition that stops recursion.
# - Recursive case → the function calls itself with a smaller/simpler input.

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Always define a base case; otherwise, recursion will go on forever and cause a RecursionError.
# Recursion is elegant but can be less efficient than loops for large inputs (because of function call overhead).

# Python has a recursion depth limit (default ~1000 calls). You can check it with:

import sys
print(sys.getrecursionlimit())