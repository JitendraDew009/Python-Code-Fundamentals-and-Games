f = open("auto_create_file.txt", "w+")
f.write("Im using w+") # Truncate = to take something short (read -> erase all -> rewrite)
f.close()