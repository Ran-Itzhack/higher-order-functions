from hof_decorator.decorator_1 import greeting, greeting_uppercase_decorator
from hof_decorator.decorator_2 import greeting
from hof.hof_1 import upper_text, lower_text, handle_text
from hof.hof_2 import make_adder
from hof.hof_3 import sum, divide, do_opr_calculator
from hof.hof_4 import sum_numbers, higher_order_function
from hof.function_as_a_return_value import hof_func_return_value

if __name__ == '__main__':
    # handle_text(lower_text)
    # print(exe1_ret())

    # HOR 2: Python Closures
    # add_three = make_adder(3)
    # print(add_three(15))
    # print(make_adder(3)(15))

    # HOR 3
    # print(do_opr_calculator(divide, 30, 10) )

    # HOR 4: Function as a Parameter
    # result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
    # print(result)

    # Function as a Return Value
    #
    # result = hof_func_return_value('square')
    # print(result(3))  # 9
    # result = hof_func_return_value('cube')
    # print(result(3))  # 27
    # result = hof_func_return_value('absolute')
    # print(result(-3))  # 3

    # Decorators 1
    # g = greeting_uppercase_decorator(greeting)
    # print(g('Welcome to Python '))  # WELCOME TO PYTHON

    # Decorators 2
    print(greeting())  # WELCOME TO PYTHON
