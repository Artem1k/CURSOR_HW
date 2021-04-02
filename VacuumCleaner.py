from Exceptions import *


class CleanerWork:
    def __new__(cls, battery, trash, water):
        if (int(battery) in range(101)) and (int(trash) in range(201)) and (int(water) in range(501)):
            return object.__new__(cls)
        try:
            raise WrongInboundData
        except WrongInboundData:
            return print('Wrong inbound data')

    def __init__(self, battery, trash, water):
        self.battery = int(battery)
        self.trash = int(trash)
        self.water = int(water)

    def move(self):
        while True:
            # time.sleep(1)
            # print('move')
            try:
                self.low_battery_check()
                self.vacuum_cleaner()
                self.wash()
            except EmptyWater:
                while True:
                    try:
                        self.low_battery_check()
                        self.vacuum_cleaner()
                    except LowBattery:
                        for i in range(20):
                            try:
                                self.vacuum_cleaner()
                            except FullTrash:
                                print('Почистіть мене від сміття!')
                                break
                    except DeadBattery:
                        print('Занесіть мене на зарядку!')
                        break
                    except FullTrash:
                        print('Почистіть мене від сміття!')
                        break
            except LowBattery:
                for i in range(20):
                    try:
                        self.vacuum_cleaner()
                        self.wash()
                    except EmptyWater:
                        while i < 19:
                            try:
                                i += 1
                                self.vacuum_cleaner()
                            except FullTrash:
                                print('Почистіть мене від сміття!')
                                break
                    except FullTrash:
                        print('Почистіть мене від сміття!')
                        break
            except DeadBattery:
                print('Занесіть мене на зарядку!')
                break
            except FullTrash:
                print('Почистіть мене від сміття!')
                break
        print('Я закінчив!')

    def wash(self):
        if self.water > 1:
            self.water -= 2
        else:
            raise EmptyWater

    def low_battery_check(self):
        if self.battery == 20:
            raise LowBattery

    def vacuum_cleaner(self):
        if self.battery > 0 and self.trash != 200:
            self.battery -= 1
        elif self.battery == 0:
            raise DeadBattery
        if self.trash < 200:
            self.trash += 1
        else:
            raise FullTrash

    def recharge(self):
        self.battery = 100

    def to_clean(self):
        self.trash = 0

    def add_water(self):
        self.water = 500
