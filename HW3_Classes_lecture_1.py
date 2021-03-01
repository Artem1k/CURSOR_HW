class Vehicle:
    def __init__(self, max_speed, mileage):
        self.__max_speed = max_speed
        self.__mileage = mileage


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        pass


# x = Bus(4, 5)
# print(x.get())
