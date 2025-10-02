# open("File.txt", "r") #read the file
# open("File.txt", "w") #write the file
# open("File.txt", "a") #append the file

example_file = open("File.txt", "r")
# print(example_file.readable()) # it gives boolean value true or not
print(example_file.read()) 
print("---------------------------")
example_file = open("file.txt", "r")
print(example_file.readlines()[0]) 
example_file.close()
