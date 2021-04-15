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
        with self.assertRaises(TypeError):
            self.user6 = Registration('Igor', ['Igor@gmail.com'], 53456780)

    def test_email_exist(self):
        for user in self.users:
            with self.assertRaises(EmailAlreadyExist):
                Registration.email_exist(user.email)
        self.assertTrue(Registration.email_exist('who@gmail.com'))

    def test_username_exist(self):
        for user in self.users:
            with self.assertRaises(UsernameAlreadyExist):
                Registration.username_exist(user.username)
        self.assertTrue(Registration.email_exist('who'))


class TestPasswordCheck(unittest.TestCase):
    def setUp(self) -> None:
        self.psw = PasswordCheck

    def test_password_spellcheck(self):
        with self.assertRaises(InvalidSymbols):
            self.psw.password_spellcheck('1234#%^#567')
            self.psw.password_spellcheck('5345.678')
        with self.assertRaises(AttributeError):
            self.psw.password_spellcheck(1234567)
            self.psw.password_spellcheck([1234567])
        with self.assertRaises(TypeError):
            self.psw.password_spellcheck()

    def test_password_len_check(self):
        with self.assertRaises(IncorrectLengthPassword):
            self.psw.password_len_check('1234#%^#567')
        with self.assertRaises(TypeError):
            self.psw.password_len_check()
            self.psw.password_len_check(1234567)
            self.psw.password_len_check([1234567])

    def test_password_short_or_long(self):
        with self.assertRaises(TypeError):
            self.psw.password_short_or_long()
            self.psw.password_short_or_long(1234567)
            self.psw.password_short_or_long([1234567])
        with self.assertRaises(TooLongPassword):
            self.psw.password_short_or_long('1234#%^#567')
        with self.assertRaises(TooShortPassword):
            self.psw.password_short_or_long('33gesw')

    def test_password_check(self):
        self.assertIsNone(self.psw.password_check('ascywegb'))
        self.assertIsNone(self.psw.password_check('1234567'))
        with self.assertRaises(TooLongPassword):
            self.psw.password_check('1234#%^#567')
        with self.assertRaises(TypeError):
            self.psw.password_check(1234567)
        with self.assertRaises(InvalidSymbols):
            self.psw.password_check('5345.678')

