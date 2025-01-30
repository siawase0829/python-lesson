def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator2
def say_hello2(name):
    print(f"Hello, {name}!")

say_hello2("John")

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(name):
    print(f"Hello, {name}!")

greet("John")

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} was called with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

@timer
def example():
    for i in range(10000000):
        pass

example()

def register(func):
    print(f"{func.__name__} was registered.")
    return func

@register
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} was called {count} times.")
        return func(*args, **kwargs)
    return wrapper

@counter
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
result = add(4, 6)
print(result)
