# generator function with yield

def serve_chai():
    yield "cup 1 : masala chai"
    yield "cup 2 : ginger chai"
    yield "cup 3 : black chai"
    yield "cup 4 : lemon chai"

serve_on_tray = serve_chai()
print(serve_on_tray) #<generator object serve_chai at 0x000001FFA6AD5A60>

print(next(serve_on_tray)) # cup 1 : masala chai

print(next(serve_on_tray)) # cup 2 : ginger chai

print(next(serve_on_tray)) # cup 3 : black chai

print(next(serve_on_tray)) # cup 4 : lemon chai

print(next(serve_on_tray)) # Error : StopIteration

# ======================================

def serve_chai2():
    yield "cup 1 : masala chai"
    yield "cup 2 : ginger chai"
    yield "cup 3 : black chai"
    yield "cup 4 : lemon chai"

serve_on_tray2 = serve_chai()
for cup in serve_on_tray2:
    print(cup)# cup 1 : masala chai
              # cup 2 : ginger chai
              # cup 3 : black chai
              # cup 4 : lemon chai
