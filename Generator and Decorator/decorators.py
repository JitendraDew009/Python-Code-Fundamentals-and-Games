def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator #placing holder of func()
def greet():
    print("Hello from decorators class from Github")

greet() #Before function runs
        # Hello from decorators class from Github
        # After function runs

# @my_decorator #placing holder of func()
# def greet():
#     print("Hello from decorators class from Github")

# greet() # Hello from decorators class from chaicode