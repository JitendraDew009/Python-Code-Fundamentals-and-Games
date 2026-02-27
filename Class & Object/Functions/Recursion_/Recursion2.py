def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    
show(10)

print("---------------------------")
def show(n):
    if (n == -1):
        return
    print(n)
    show(n-1)
    print("END")

show(3)

print("---------------------------")
n = 10
for i in range(1,n+1):
    rev = n - i
    if rev == 0:
        break
    print(rev)