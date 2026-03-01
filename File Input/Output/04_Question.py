# WAF to find in which in line of the file does the word "learning" occur first. Print  -1 if word not found.

def check_for_line():
    
    line_no = 1
    data = True
    word = "learning"
    
    with open("practice_file.txt", "r") as f:
        while data:
            data = f.readline()    
            if(word in data):
                print(line_no)
                return 
                line_no += 1
    return -1   

print(check_for_line())
