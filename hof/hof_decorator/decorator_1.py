# Normal function
def greeting(value):
    return 'Welcome to Python ' + value


def greeting_uppercase_decorator(function):
    value = 'decorator'

    def wrapper():
        func = function(value)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
