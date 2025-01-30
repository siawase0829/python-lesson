# Define a decorator function
def my_decorator(func):
    def wrapper():
        # Code to be executed before the function is called
        print("Something is happening before the function is called.")
        func()
        # Code to be executed after the function is called
        print("Something is happening after the function is called.")
    return wrapper

# Define a function to test the decorator
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
