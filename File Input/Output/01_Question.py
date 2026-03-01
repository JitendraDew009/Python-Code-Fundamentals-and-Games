# Write a function that replaces all occurrences of "Python" with  "Java" in above file.
with open("practice_file2.txt", "r") as f:
    data = f.read()
    new_data = data.replace("python", "Java") # python will be replaced by Java
    print(new_data)

    with open("practice_file2.txt", "w") as f:
        f.write(new_data)