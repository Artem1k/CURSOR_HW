import unittest
from Registration import *


class TestRegistration(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.user1 = Registration('Artem', 'artemboyko2002@gmail.com', '1234567')
    #     self.user2 = Registration('Maxim', 'maxim@gmail.com', 'ascywegb')
    #     self.user3 = Registration()
    #     self.user4 = Registration('Artem', 'artem2000@gmail.com', '1234567')
    #     self.user5 = Registration('Bodya', 'bodya@gmail.com', '1234#%^#567')

    def test_new(self):
        self.user1 = Registration('Artem', 'artemboyko2002@gmail.com', '1234567')
        self.user2 = Registration('Maxim', 'maxim@gmail.com', 'ascywegb')
        self.user3 = Registration()
        self.user4 = Registration('Artem', 'artem2000@gmail.com', '1234567')
        self.user5 = Registration('Bodya', 'bodya@gmail.com', '1234#%^#567')
        self.user6 = Registration('Igor', ['Igor@gmail.com'], '5345.678')

