# Default parameter Value:
# Write a fuction that greets a user. If no name is provided, it should greet with a default name.

def greet():
    name = input("Enter Your Name:")
    if name == '':
        print("Hi User!")
    else:
        print("Hi " + name + "!")
    return greet

greet()

# Alernate Solution
print("\n # Alernate Solution")
def greet(name = "User"):
    return "Hello " + name + "!"

print(greet("Samurai")) #Hello Samurai!
print(greet()) #User