def decorator_function(func):
    def wrapper():
        print("Executing some code before the original function.")
        func()
        print("Executing some code after the original function.")

    return wrapper


@decorator_function
def greeting_2():
    print("Hello, World!")