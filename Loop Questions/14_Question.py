# You have preparing an oder summary with customer names and their total bill.
# Task : Use two lists : one for name and ane for bills.
#        print :"[Names] paid Rs.[amount]"
#  Use Zip() 
names = ['Jitendra', 'Jitesh', 'Pawan', 'Samuel', 'Durgesh']
bills = [50, 40, 25, 100, 80]

for name, amount in zip(names,bills):
    print(f"{name} paid Rs. {amount}")