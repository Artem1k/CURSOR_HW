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


School_bus = Bus(4, 5, 6)
print(f'class of School_bus is {type(School_bus)}')
# 3.Output: class of bus_object is <class '__main__.Bus'>
if isinstance(School_bus, Vehicle):
    print('School_bus is also instance Vehicle')
# 4.Output: School_bus is also instance Vehicle
bear = Bear()
wolf = Wolf()
tuple_of_animals = bear, wolf
for i in tuple_of_animals:
    i.make_sound()
