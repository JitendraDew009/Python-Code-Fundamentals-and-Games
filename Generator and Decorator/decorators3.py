from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator #placing holder of func()
def greet():
    print("Hello from decorators class from Github")

greet() 
print(greet.__name__) #greet

# It just a wrapper fucntion which takes your fucntion, execute it and probably adds some more to it.
# probably checks more things, jsut the printing statement, inject or extract more values.