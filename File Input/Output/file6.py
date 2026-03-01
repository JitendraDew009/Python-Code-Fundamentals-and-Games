f = open("auto_create_file.txt", "r+")
f.write("Im using r+") # No Truncate; (read -> overwrite)
f.close()