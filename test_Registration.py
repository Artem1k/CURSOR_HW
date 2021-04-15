import unittest
from Registration import *


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        self.user1 = Registration('Artem', 'artemboyko2002@gmail.com', '1234567')
        self.user2 = Registration('Maxim', 'maxim@gmail.com', 'ascywegb')
        self.users = [self.user1, self.user2]

    def test_init_new(self):
        self.user1 = Registration('Artem', 'artemboyko2002@gmail.com', '1234567')
        self.user2 = Registration('Maxim', 'maxim@gmail.com', 'ascywegb')
        self.user3 = Registration()
        self.user4 = Registration('Artem', 'artem2000@gmail.com', '1234567')
        self.user5 = Registration('Bodya', 'bodya@gmail.com', '1234#%^#567')
        self.user6 = Registration('Igor', ['Igor@gmail.com'], '5345.678')

    def test_email_exist(self):
        for user in self.users:
            with self.assertRaises(EmailAlreadyExist):
                Registration.email_exist(user.email)

    def test_username_exist(self):
        for user in self.users:
            with self.assertRaises(UsernameAlreadyExist):
                Registration.username_exist(user.username)
