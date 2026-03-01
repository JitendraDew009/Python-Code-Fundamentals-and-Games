# Write a program that counts number of even number from a file.

count = 0
with open("practice_file3.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)