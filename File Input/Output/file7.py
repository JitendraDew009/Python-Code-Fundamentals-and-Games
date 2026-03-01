with open("auto_create_file.txt", "r") as f:
    data = f.read()
    print(data)
    #there is no need of f.close() because it has bilt feature of closing file. 

with open("auto_create_file.txt", "w") as f:
    data = f.write("NEW DATA FOUND ----") #writing new data
    print(data) #19 -> your length of string.

#there is no need of f.close() because it has biult feature of closing file. 