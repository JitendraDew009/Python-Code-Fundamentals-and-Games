def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator #placing holder of func()
def greet():
    print("Hello from decorators class from Github")

greet() 
print(greet.__name__) #wrapper