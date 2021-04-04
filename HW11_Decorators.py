from functools import wraps

print('1.')


# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    @wraps(func)
    def inner(a, b):
        result = func(a, b)
        return result * 2

    return inner


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20

# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"
print('\n2.')


def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    @wraps(func)
    def inner(*args):
        for i in args:
            if i % 2 == 0:
                return print("Please use only odd numbers!")
        return func(*args)

    return inner


@only_odd_parameters
def add(a, b):
    return print(a + b)


add(5, 5)  # 10
add(4, 4)  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):
print('\n3.')
import logging

log_format = ' %(asctime)s - %(name)s - %(levelname)s -%(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)


def logged(func):
    @wraps(func)
    def inner(*args):
        """
        logged
        :param args:
        :return: func
        """
        logging.info(f'Calling {func.__name__}')
        logging.info(f'The doc string of this func ic {func.__doc__}')
        logging.info(f'This func otakes {args}')
        return print(func(*args))

    return inner


@logged
def func(*args):
    """
    :param args:
    :return: 3 + len(args)
    """
    return 3 + len(args)


func(4, 4, 4)
print(func.__name__)
print(func.__doc__)
# you called func(4, 4, 4)
# it returned 6

# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.
print('\n4.')


def type_check(correct_type):
    def type_check_decorator(func):
        @wraps(func)
        def inner(a):
            """
            type_check inner
            :param a:
            :return:
            """
            if isinstance(a, correct_type):
                return func(a)
            return print(f'"Wrong Type: {a.__class__.__name__}" should be printed, '
                         f'since non-{correct_type.__name__} passed to decorated function')

        return inner

    return type_check_decorator


@type_check(int)
def times2(num):
    """
    :param num:
    :return: num + 2
    """
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    """
    :param word:
    :return: word[0]
    """
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
