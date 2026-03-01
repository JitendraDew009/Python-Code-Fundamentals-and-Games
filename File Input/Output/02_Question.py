word = "learning"
with open("practice_file.txt", "r") as f:
    data = f.read()
   
    if(data.find(word) != -1):
       print("FOUND")
    else:
        print("NOT FOUND")
       