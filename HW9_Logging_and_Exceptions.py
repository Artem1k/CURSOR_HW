import logging
import inspect
import time

time.asctime()
log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s'
logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="w", format=log_template)
# logger = logging.getLogger(__name__)
#
# # Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log', 'w')
#
# c_handler.setLevel(logging.ERROR)
# f_handler.setLevel(logging.DEBUG)
#
# # Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)
#
# # Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
print('Це калькулятор!')


# Task 1
def number():
    while True:
        str_num = input('')
        logging.info(f'str_num in def number(): {str_num}. '
                     f'- {inspect.stack()[1].code_context[0][-1]} in line: {inspect.stack()[1].lineno}')
        try:
            num = int(str_num)
            break
        except ValueError:
            logging.error('ValueError in def number()')
            print('ValueError')
    logging.info(f'num in def number(): {num}. '
                 f'- {inspect.stack()[1].code_context[0][-1]} in line: {inspect.stack()[1].lineno}')
    return num


while True:
    str_point = input('Що ви хочете виконати?\n1.Додавання\n2.Віднімання\n3.Множення\n4.Ділення\n'
                      '5.Піднесення в степінь\n6.Взяття з під кореня\n7.Пошук відсотку від числа\n8.Exit\n')
    logging.info(f'str_point: {str_point}')
    try:
        point = int(str_point)
    except ValueError:
        logging.error('ValueError when tried to int(str_point)')
        print('Incorrect!')
    if point == 1:
        print('Введіть перший доданок: ', end='')
        num1 = number()
        print('Введіть другий доданок: ', end='')
        num2 = number()
        result = num1 + num2
        logging.info(f'Сума: {result}')
        print(f'Сума: {result}')
    elif point == 2:
        print('Введіть зменшуване: ', end='')
        num1 = number()
        print('Введіть від\'ємник: ', end='')
        num2 = number()
        result = num1 - num2
        logging.info(f'Різниця: {result}')
        print(f'Різниця: {result}')
    elif point == 3:
        print('Введіть перший множник: ', end='')
        num1 = number()
        print('Введіть другий множник: ', end='')
        num2 = number()
        result = num1 * num2
        logging.info(f'Добуток: {result}')
        print(f'Добуток: {result}')
    elif point == 4:
        print('Введіть ділене: ', end='')
        num1 = number()
        print('Введіть дільник: ', end='')
        num2 = number()
        try:
            result = num1 / num2
        except ZeroDivisionError:
            logging.warning('ZeroDivisionError')
            result = 'infinity'
        logging.info(f'Частка: {result}')
        print(f'Частка: {result}')
    elif point == 5:
        print('Введіть число: ', end='')
        num1 = number()
        print('Введіть степінь: ', end='')
        num2 = number()
        result = num1 ** num2
        logging.info(f'Результат: {result}')
        print(f'Результат: {result}')
    elif point == 6:
        print('Введіть число: ', end='')
        num1 = number()
        print('Введіть степінь кореня: ', end='')
        num2 = number()
        result = num1 ** (1 / num2)
        logging.info(f'Результат: {result}')
        print(f'Результат: {result}')
    elif point == 7:
        def sub_number():
            while True:
                num = number()
                if num < 0:
                    print('Відсоток не може бути мінусовий')
                else:
                    return num
                    break


        print('Введіть число: ', end='')
        num1 = number()
        print('Введіть відсотки: ', end='')
        num2 = sub_number()
        result = num1 * (num2 / 100)
        logging.info(f'Результат: {result}')
        print(f'Результат: {result}')
    elif point == 8:
        logging.info('exit')
        print('exit')
        break
    else:
        logging.warning(f'Incorrect number of act!')
        print('Incorrect!')


'''Це калькулятор!
Що ви хочете виконати?
1.Додавання
2.Віднімання
3.Множення
4.Ділення
5.Піднесення в степінь
6.Взяття з під кореня
7.Пошук відсотку від числа
8.Exit
1
Введіть перший доданок: 4
Введіть другий доданок: h
ValueError
6
Сума: 10
Що ви хочете виконати?
1.Додавання
2.Віднімання
3.Множення
4.Ділення
5.Піднесення в степінь
6.Взяття з під кореня
7.Пошук відсотку від числа
8.Exit
7
Введіть число: 100
Введіть відсотки: -5
Процент не може бути мінусовий
5
Результат: 5.0
Що ви хочете виконати?
1.Додавання
2.Віднімання
3.Множення
4.Ділення
5.Піднесення в степінь
6.Взяття з під кореня
7.Пошук відсотку від числа
8.Exit
4
Введіть ділене: 5
Введіть дільник: 0
Частка: infinity
Що ви хочете виконати?
1.Додавання
2.Віднімання
3.Множення
4.Ділення
5.Піднесення в степінь
6.Взяття з під кореня
7.Пошук відсотку від числа
8.Exit
6
Введіть число: 25
Введіть степінь кореня: 2
Результат: 5.0
Що ви хочете виконати?
1.Додавання
2.Віднімання
3.Множення
4.Ділення
5.Піднесення в степінь
6.Взяття з під кореня
7.Пошук відсотку від числа
8.Exit
8
exit
'''


# Task 2
class LowBattery(Exception):
    pass


class DeadBattery(Exception):
    pass


class EmptyWater(Exception):
    pass


class FullTrash(Exception):
    pass


class CleanerWork:
    def __init__(self, battery, trash, water):
        self.battery = battery
        self.trash = trash
        self.water = water

    def move(self):
        while True:
            time.sleep(1)
            print('move')
            try:
                self.vacuum_cleaner()
                self.wash()
            except EmptyWater:
                while True:
                    try:
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
                        for j in range(20 - i):
                            try:
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

    def vacuum_cleaner(self):
        if self.battery == 20:
            raise LowBattery
        if self.battery > 0:
            self.battery -= 1
        else:
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


vacuum_water = 500
vacuum_trash = 0
vacuum_battery = 100
