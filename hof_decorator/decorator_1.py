# Normal function
def greeting(value1: str, value2: str) -> str:
    return value1 + value2


def greeting_uppercase_decorator(function):
    value = 'decorator'

    def wrapper(params: str) -> str:
        func = function(params, value)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
