'''4. Divide the work between 2 methods: print_cube that returns the cube of number
and print_square that returns the square of number.
These two methods should be executed by using 2 different processes.'''
from concurrent.futures import ProcessPoolExecutor


def print_cube(x):
    return print(x ** 3)


def print_square(x):
    return print(x ** 2)


with ProcessPoolExecutor(max_workers=2) as ex:
    ex.submit(print_cube, 2)
    ex.submit(print_square, 2)
