import unittest
from Registration import *


class TestRegistration(unittest.TestCase):
    parameters = [['Artem', 'artemboyko2002@gmail.com', '1234567'],
                  ['Maxim', 'maxim@gmail.com', 'ascywegb'],
                  [],
                  ['Artem', 'artem2000@gmail.com', '1234567'],
                  ['Bodya', 'bodya@gmail.com', '1234#%^#567'],
                  ['Igor', 'Igor@gmail.com', 53456780],
                  ['Igor', ['Igor@gmail.com'], '5345.678']]

    def setUp(self) -> None:
        self.user = Registration()
        # self.user2 = Registration('Maxim', 'maxim@gmail.com', 'ascywegb')
        # self.users = [self.user1, self.user2]

    # def test_init_new(self):
    #     self.user1 = Registration('Artem', 'artemboyko2002@gmail.com', '1234567')
    #     self.user2 = Registration('Maxim', 'maxim@gmail.com', 'ascywegb')
    #     self.user3 = Registration()
    #     self.user4 = Registration('Artem', 'artem2000@gmail.com', '1234567')
    #     self.user5 = Registration('Bodya', 'bodya@gmail.com', '1234#%^#567')
    #     with self.assertRaises(TypeError):
    #         self.user6 = Registration('Igor', 'Igor@gmail.com', 53456780)
    #         self.user6 = Registration('Igor', ['Igor@gmail.com'], '5345.678')

    def test_call(self):
        with self.assertRaises(TypeError):
            for user in self.parameters[-2:-1]:
                self.user(user)

    def test_email_exist(self):
        self.assertTrue(Registration.email_exist('who@gmail.com'))
        self.user('who', 'who@gmail.com', '12345678')
        with self.assertRaises(EmailAlreadyExist):
            Registration.email_exist('who@gmail.com')

    def test_username_exist(self):
        self.assertTrue(Registration.email_exist('what'))
        self.user('what', 'what@gmail.com', '12345678')
        with self.assertRaises(UsernameAlreadyExist):
            Registration.username_exist('what')


class TestUserToken(unittest.TestCase):
    def setUp(self) -> None:
        self.user = Registration()
        self.user_token = UserToken()
        self.user('Artem', 'artemboyko2002@gmail.com', '1234567')
        self.user('Maxim', 'maxim@gmail.com', 'ascywegb')

    def test_new(self):
        self.user_token('artemboyko2002@gmail.com', '1234567')
        self.user_token('maxim@gmail.com', 'ascywegb')
        with self.assertRaises(KeyError):
            self.user_token('bodya@gmail.com', '1234#%^#567')
        with self.assertRaises(InvalidNameOrPassword):
            self.user_token('artemboyko2002@gmail.com', 'ascywegb')


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
