class Vehicle:
    def __init__(self, max_speed, mileage):
        self.__max_speed = max_speed
        self.__mileage = mileage


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.__seating_capacity = seating_capacity
        super().__init__(max_speed, mileage)
    # def seating_capacity(self):
    #     pass


class School:
    def __init__(self, get_school_id, number_of_students):
        self.__get_school_id = get_school_id
        self.__number_of_students = number_of_students


class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        self.__bus_school_color = bus_school_color
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)


class Bear:
    def make_sound(self):
        return print("Bear sounds")


class Wolf:
    def make_sound(self):
        return print("Wolf sounds")


class City:

    def __init__(self, name, population):
        self.__name = name
        self.__population = population

    def __new__(cls, name, population):
        print("Creating Instance")
        instance = super(City, cls).__new__(cls)
        if population <= 1500:
            return print('Your city is too small')
        else:
            return instance

    def __str__(self):
        return f'The population of the city {self.__name} is {self.__population}'


School_bus = Bus(4, 5, 6)
print(f'class of School_bus is {type(School_bus)}')
# 3.Output: class of bus_object is <class '__main__.Bus'>
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
#     instance = super(City, cls).__new__(cls)
#     if population > 1500:
#         return instance
#     else:
#         return 'Your city is too small'
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
