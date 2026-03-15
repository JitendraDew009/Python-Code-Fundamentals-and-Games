def local_chai():
    yield "masala chai"
    yield "ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():

    try:
        while True:
            order = yield "Waiting for chai order"
    except: # catch / except
        print("Stall closed, No more chai")

stall = chai_stall()
print(next(stall))
# masala chai
# ginger chai
# Matcha
# Oolong
# Waiting for chai order
# Stall closed, No more chai
print("---It is still running behind the scene so you have to close this to save the memory---")
stall.close()