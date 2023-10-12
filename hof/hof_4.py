from typing import List

# https://github.com/deeplearninghumans/50-Days-Of-Python-Data-Structure-Algorithms/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md#python-decorators


def sum_numbers(nums: List[int]) -> int:
    return sum(nums)


def higher_order_function(func, *args):
    summation = func(*args)
    return summation
