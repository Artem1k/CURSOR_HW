from Exceptions import *


class Registration:
    USERS = {}
    usernames = []

    # def __new__(cls, *args, **kwargs):
    #     try:
    #         username, email, psw = args
    #     except ValueError:
    #         return print('400\nValueError')
    #     try:
    #         cls.email_exist(email)
    #     except EmailAlreadyExist:
    #         return print('400\nThis email already exist')
    #     try:
    #         cls.username_exist(username)
    #     except UsernameAlreadyExist:
    #         return print('400\nThis username already exist')
    #     else:
    #         try:
    #             PasswordCheck.password_check(psw)
    #             cls.USERS[email] = psw
    #             cls.usernames.append(username)
    #             return super().__new__(cls)
    #             # return print('200')
    #         except TooShortPassword:
    #             return print('TooShortPassword')
    #         except TooLongPassword:
    #             return print('TooLongPassword')
    #         except InvalidSymbols:
    #             return print('400\nInvalidPassword')

    def __call__(self, username, email, password):
        self.email_exist(email)
        self.username_exist(username)
        PasswordCheck.password_check(password)
        self.USERS[email] = password
        self.usernames.append(username)
        return '200'

    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.psw = password
    #     self.data = [self.username, self.email, self.psw]
    #     print('200')

    @staticmethod
    def email_exist(email):
        if email in Registration.USERS.keys():
            raise EmailAlreadyExist
        else:
            return True

    @staticmethod
    def username_exist(username):
        if username in Registration.usernames:
            raise UsernameAlreadyExist
        else:
            return True


class UserToken:
    # def __new__(cls, *args, **kwargs):
    #     try:
    #         email, psw = args
    #     except ValueError:
    #         return print('400\nValueError')
    #     if Registration.USERS[email] == psw:
    #         return super().__new__(cls)
    #     else:
    #         raise InvalidNameOrPassword

    # def __init__(self, email, password):
    #     print("Correct")

    def __call__(self, email, password):
        if Registration.USERS[email] == password:
            return '200'
        else:
            raise InvalidNameOrPassword


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
        # except TypeError:
        #     print('400\nTypeError')
