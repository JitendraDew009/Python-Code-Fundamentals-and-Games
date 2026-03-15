def chai_pour(n):
    print(n)
    if n == 0:
        return "All cups are poured"
    return chai_pour(n-1) # see you are call itself multiple times.

print(chai_pour(3))
