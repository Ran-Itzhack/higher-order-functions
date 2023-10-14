# https://github.com/deeplearninghumans/50-Days-Of-Python-Data-Structure-Algorithms/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md#function-as-a-return-value

def decorator_function(function):
    local_value = 'decorator '

    def wrapper(*args, **kwargs) -> int:
        print("Started")
        result = function(local_value, *args, **kwargs)
        print("Ended")
        return result
        # "Ended"

    return wrapper


@decorator_function
def greeting_uppercase(value1: str, value2='abc'):
    msg = (value2 + value1).upper()
    print(msg)
    # return value1 + value2 + x


@decorator_function
def add(a, x: int, y: int) -> int:
    return x + y
