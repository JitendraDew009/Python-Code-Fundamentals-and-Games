# 19. Building a pyramid in python
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end= "")
    for j in range(i+1):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    print("") 
    
#------------------------
# The pyramid is symmetric because:

# Left stars: i + 1

# Right stars: i

# Total stars per row: 2i + 1

# Spaces decrease as i increases, keeping the pyramid centered
# ----------------------------------------------------------------------
def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
pyramid(5)


