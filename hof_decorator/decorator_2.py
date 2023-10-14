# https://github.com/deeplearninghumans/50-Days-Of-Python-Data-Structure-Algorithms/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md#function-as-a-return-value

def greeting_uppercase_decorator(function):
    value = 'decorator '

    def wrapper(*args, **kwargs):
        print("Started")
        func = function(value, *args, **kwargs)
        make_uppercase = func.upper()
        return make_uppercase
        # "Ended"

    return wrapper


@greeting_uppercase_decorator
def greeting(value1: str, value2: str, x) -> str:
    return value1 + value2 + x


@greeting_uppercase_decorator
def add(x: int, y: int) -> int:
    return x + y
