# make fuction of print EVEN or ODD number by taking input from user 
def number():
    num = int(input("Enter any number :"))
    if (num % 2 == 0 ):
        print("EVEN NUMBER")
    else:
        print("ODD NUMBER")
    return num

number()
