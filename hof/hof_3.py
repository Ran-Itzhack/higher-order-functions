from typing import Dict, Optional


def sum(x: int, y: int) -> int:
    return x + y


def divide(x: int, y: int) -> float:
    assert y != 0, "That is false!"
    return x / y


def do_opr_calculator(op_func, x: int, y: int) -> int:
    return op_func(x, y)

#
# def handle_text(func):
#     text = func("Hello world!")
#     print(text)
