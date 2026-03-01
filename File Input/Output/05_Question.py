# From a file containing numbers seperated by comma, print the count of even number.

with open("practice_file3.txt", "r") as f:
    data = f.read()
    print(data) # i  string (reult)
    num = ""
    for i in range(len(data)):
        if (data [i] == "," ):
            print(int(num))
            num = ""
        else:
            num += data[i]


with open("practice_file3.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    print(nums)