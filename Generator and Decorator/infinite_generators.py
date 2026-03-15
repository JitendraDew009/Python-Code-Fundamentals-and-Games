def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()

user2 = infinite_chai()

for cup in range(5):
    print(next(refill))

print("===User2===")

# May in future any new user want different.
for cup in range(8):
    print(next(user2))

