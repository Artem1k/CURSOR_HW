from Exceptions import *


class Registration:
    users_email = []
    usernames = []

    def __new__(cls, *args, **kwargs):
        try:
            username, email, psw = args
        except ValueError:
            return print('400\nValueError')
        try:
            cls.email_exist(email)
        except EmailAlreadyExist:
            return print('400\nThis email already exist')
        try:
            cls.username_exist(username)
        except UsernameAlreadyExist:
            return print('400\nThis username already exist')
        else:
            try:
                PasswordCheck.password_check(psw)
                cls.users_email.append(email)
                cls.usernames.append(username)
                instance = super().__new__(cls)
                instance.__init__(username, email, psw)
                return print('200')
            except TooShortPassword:
                return print('TooShortPassword')
            except TooLongPassword:
                return print('TooLongPassword')
            except InvalidSymbols:
                return print('400\nInvalidPassword')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.psw = password
        self.data = [self.username, self.email, self.psw]

    def __str__(self):
        return f'Your username: {self.username}\nYour email: {self.email}'

    @classmethod
    def email_exist(cls, email):
        if email in cls.users_email:
            raise EmailAlreadyExist
        else:
            return True
    @classmethod
    def username_exist(cls, username):
        if username in cls.usernames:
            raise UsernameAlreadyExist
        else:
            return True

class PasswordCheck:
    @staticmethod
    def password_spellcheck(psw):
        if psw.isalnum():
            return True
        else:
            raise InvalidSymbols

    @staticmethod
    def password_len_check(psw):
        if len(psw) in range(7, 9):
            return True
        else:
            raise IncorrectLengthPassword

    @staticmethod
    def password_short_or_long(psw):
        if len(psw) < 7:
            raise TooShortPassword
        else:
            raise TooLongPassword

    @staticmethod
    def password_check(psw):
        try:
            PasswordCheck.password_len_check(psw)
            PasswordCheck.password_spellcheck(psw)
        except IncorrectLengthPassword:
            print('400\nIncorrectLengthPassword')
            PasswordCheck.password_short_or_long(psw)

