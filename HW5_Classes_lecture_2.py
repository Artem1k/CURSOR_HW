# 1.
class Laptop:
    """
    Make the class with composition.
    """

    def __init__(self, mah):
        self._mah = Battery(mah)

    def do(self):
        print(self._mah)


class Battery:
    """
    Make the class with composition.
    """

    def __init__(self, mah):
        self._mah = mah

    # below will another example such like this
    def __str__(self):
        return f'{self._mah}'


print('1. ', end='')
lenovo = Laptop(5000)
lenovo.do()
# Output: 1. 5000


# 2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, strings):
        self._strings = strings

    def info(self):
        print(self._strings)


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, number_of_strings, material):
        self._number_of_strings = number_of_strings
        self._material = material

    # Here
    def __str__(self):
        return 'number_of_strings: ' + str(self._number_of_strings) + '\nmaterial: ' + self._material


print('2.')
string = GuitarString(6, 'metal')
guitar = Guitar(string)
guitar.info()
'''Output: 2.
number_of_strings: 6
material: metal'''
