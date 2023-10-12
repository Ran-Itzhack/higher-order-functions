def square(x):  # a square function
    return x ** 2


def cube(x):  # a cube function
    return x ** 3


def absolute(x):  # an absolute value function
    if x >= 0:
        return x
    else:
        return -x


def hof_func_return_value(func_type):  # a higher order function returning a function
    if func_type == 'square':
        return square
    elif func_type == 'cube':
        return cube
    elif func_type == 'absolute':
        return absolute


# result = hof_func_return_value('square')
# print(result(3))  # 9
# result = hof_func_return_value('cube')
# print(result(3))  # 27
# result = hof_func_return_value('absolute')
# print(result(-3))  # 3
