# number of factoril
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    return fact #gives back a value (data you can use later)

calc_fact(12)

