number_grid = [
 [1,2,3,],
 [4,5,6],
 [7,8,9],
 [0]
]
print(number_grid[2][1]) # 8
print(number_grid[0][0]) # 1
print(number_grid[2][2]) # 9

for row in number_grid:
    for col in number_grid:
        print(number_grid)

print("--------------------")
for row in number_grid:
    for col in row:
        print(col)