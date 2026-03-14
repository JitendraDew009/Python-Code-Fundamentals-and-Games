try:
    value = 10/0
    number = int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError :
    print("Divided by Zero")
except ZeroDivisionError as err :
    print(err) # yaha jo bhi error hoga vo bta dega
except ValueError : #in exept we can you space here
    print("Invalid Input")
