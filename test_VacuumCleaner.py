import unittest
from VacuumCleaner import *


class TestCleanerWork(unittest.TestCase):
    def setUp(self) -> None:
        self.cleaner_1 = CleanerWork(100, 200, 500)
        self.cleaner_2 = CleanerWork(50, 35, 200)
        self.cleaner_3 = CleanerWork('75', 110.5, 250.9)
        self.cleaner_4 = CleanerWork('0', 0.0, 0)
        self.cleaners = [self.cleaner_1, self.cleaner_2, self.cleaner_3, self.cleaner_4]

    def test_init(self):
        with self.assertRaises(ValueError):
            CleanerWork('one', 0, 0)
            CleanerWork(-1, -1, 1000)
        for cleaner in self.cleaners:
            self.assertIsInstance(cleaner.battery, int)
            self.assertIsInstance(cleaner.trash, int)
            self.assertIsInstance(cleaner.water, int)

    def test_move(self):
        for cleaner in self.cleaners:
            with self.subTest(battery=cleaner.battery, trash=cleaner.trash, water=cleaner.water):
                cleaner.move()

    def test_wash(self):
        for cleaner in self.cleaners:
            try:
                cleaner.wash()
            except EmptyWater:
                continue

    def test_low_battery_check(self):
        for cleaner in self.cleaners:
            cleaner.low_battery_check()

    def test_vacuum_cleaner(self):
        for cleaner in self.cleaners:
            with self.subTest(battery=cleaner.battery, trash=cleaner.trash, water=cleaner.water):
                try:
                    cleaner.vacuum_cleaner()
                except FullTrash:
                    continue
                except DeadBattery:
                    continue

    def test_recharge(self):
        for cleaner in self.cleaners:
            cleaner.recharge()

    def test_to_clean(self):
        for cleaner in self.cleaners:
            cleaner.to_clean()

    def test_add_water(self):
        for cleaner in self.cleaners:
            cleaner.add_water()
