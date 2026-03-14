# find factorial of n number using recursion

def factorial(n):
    if n == 0: #base case or stopping case
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))