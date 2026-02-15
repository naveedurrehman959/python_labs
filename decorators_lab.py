# Task 2: Writing a basic decorator

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper
# Task 3: Applying the decorator

@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")
# Call the function
say_hello("Alice")

