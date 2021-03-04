# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.__max_speed = max_speed
        self.__mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables
# and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.__seating_capacity = seating_capacity
        super().__init__(max_speed, mileage)

    def get_seating_capacity(self):
        return self.__seating_capacity


# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_students):
        self.__get_school_id = get_school_id
        self.__number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus
# and will have its own - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        self.__bus_school_color = bus_school_color
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
class Bear:
    def make_sound(self):
        return print("Bear sounds")


class Wolf:
    def make_sound(self):
        return print("Wolf sounds")


# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
class City:

    def __init__(self, name, population):
        self.__name = name
        self.__population = population

    def __new__(cls, name, population):
        print("Creating Instance")
        instance = super(City, cls).__new__(cls)
        if population <= 1500:
            return 'Your city is too small'
        else:
            return instance

    # 9. Override a printable string representation of the City class and return:
    # The population of the city {name} is {population}
    def __str__(self):
        return f'The population of the city {self.__name} is {self.__population}'

    # 10*. Override magic method __add__() to perform the additional action as 'multiply' (*)
    # the value which is greater than 10. And perform this add (+) of two instances.
    def __add__(self, x):
        return self.__population * x if x > 10 else self.__population + x


# 11. Create a new class with __call__ method and define this call to return sum.
class Sum:
    def __call__(self, *args):
        return sum(args)


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
class MyOrder:
    def __init__(self, cart, customer):
        self.__cart = cart
        self.__customer = customer

    def __bool__(self):
        return True if len(self.__cart) != 0 else False


# 3. Determine which class a given Bus object belongs to (Check type of an object)
School_bus = Bus(4, 5, 6)
print(f'class of School_bus is {type(School_bus)}')
# 3.Output: class of bus_object is <class '__main__.Bus'>

# 4. Determine if School_bus is also an instance of the Vehicle class
if isinstance(School_bus, Vehicle):
    print('School_bus is also instance Vehicle')
# 4.Output: School_bus is also instance Vehicle

bear = Bear()
wolf = Wolf()
tuple_of_animals = bear, wolf
for animals in tuple_of_animals:
    animals.make_sound()
''' 7.Output:
Bear sounds
Wolf sounds'''

people_1 = City('Lviv', 100000)
print(people_1)
people_2 = City('Kyiv', 1000)
if people_2:
    print(people_2)
'''8.;9.Output: 
Creating Instance
City Lviv: 100000 population
Creating Instance
Your city is too small'''

print("10.1", people_1 + 9)
print("10.2", people_1 + 11)
''' 10.Output:
10.1 100009
10.2 1100000'''

summer = Sum()
print(summer(5, 10))
# 11. Output: 15

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))
''' 12. Output:
True
False'''
