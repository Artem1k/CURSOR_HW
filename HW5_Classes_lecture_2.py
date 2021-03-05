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
'''Output: 1. 5000'''


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


# 3.
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """

    @staticmethod
    def add_nums(num1, num2, num3):
        return num1 + num2 + num3


print('3.', Calc.add_nums(1, 2, 3))
'''Output: 3. 6'''


# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, ingredients):
        self._ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])

    def __call__(self):
        print(self._ingredients)


print('4.')
pasta_1 = Pasta(["tomato", "cucumber"])
pasta_1()
pasta_2 = Pasta.bolognaise()
pasta_2()
'''Output: 4.
['tomato', 'cucumber']
['bacon', 'parmesan', 'eggs']'''


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        self._visitors_count = value if value <= self.max_visitors_num else Concert.max_visitors_num  # or self.max_...


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print('5.', concert.visitors_count)  # 50
'''Output: 5. 50'''

# 6.
import dataclasses


@dataclasses.dataclass()
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
    birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7. Create the same class (6) but using NamedTuple
import collections

AddressBookDataClassTuple = collections.namedtuple('AddressBookDataClassTuple', ['key', 'name', 'phone_number',
                                                                                 'address', 'email', 'birthday', 'age'])


# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """

    def __init__(self, key: int, name: str, phone_number: str, address: str, email: str, birthday: str, age: int):
        self._key = key
        self._name = name
        self._phone_number = phone_number
        self._address = address
        self._email = email
        self._birthday = birthday
        self._age = age

    def __str__(self):
        return f'key: {self._key}, name: {self._name}, phone_number: {self._phone_number}, ' \
               f'address: {self._address}, email: {self._email}, birthday: {self._birthday}, age: {self._age})'


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person_object = Person()
setattr(person_object, 'age', 18)
print('9.', person_object.age)
'''Output: 9. 18'''


# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(0, '')
student.email = 'student@gmail.com'
print('10.', getattr(student, 'email'))
'''Output: 10. student@gmail.com'''


# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


# create an object
obj = Celsius(36)
print('11.', obj.temperature)
'''Output: 11. 96.8'''
