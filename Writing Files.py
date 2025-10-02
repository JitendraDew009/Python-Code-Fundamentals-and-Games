# example_file = open("file.txt", "w") 
# If I put w then it will overwrite the file and new data will be added on everyrthing existing file like fresh page.

# example_file = open("file.txt", "a") #append the file is basically modefiying the file at the end of the file
# print(example_file.write("\nPop...."))
# example_file.close()

example_file = open("index.html", "w") # we are adding paragrah on index.html file.
print(example_file.write("<p>This is html page and you can edit now.</p>"))
example_file.close()