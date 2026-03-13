staff = [('Amit', 16), ("Bunny", 15), ("Cathrine", 17), ("Dakota", 18)]

for name, age in staff:
    if age <= 18 :
        print(f"{name} is eligible to manage the staff.")
        break
else: # else block only run if the loop didn't break
    print("No one is eligible to manage the staff")

# with break only Amit will get chance to get print but
# Without break : Every one will get chance and 