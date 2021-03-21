print('Це калькулятор!')


def number():
    while True:
        str_num = input('')
        try:
            num = int(str_num)
            break
        except ValueError:
            print('ValueError')
    return num


while True:
    point = input('Що ви хочете виконати?\n1.Додавання\n2.Віднімання\n3.Множення\n4.Ділення\n'
                  '5.Піднесення в степінь\n6.Взяття з під кореня\n7.Пошук відсотку від числа\n8.Exit\n')
    if point == '1':
        print('Введіть перший доданок: ', end='')
        num1 = number()
        print('Введіть другий доданок: ', end='')
        num2 = number()
        result = num1 + num2
        print(f'Сума: {result}')
    elif point == '2':
        print('Введіть зменшуване: ', end='')
        num1 = number()
        print('Введіть від\'ємник: ', end='')
        num2 = number()
        result = num1 - num2
        print(f'Різниця: {result}')
    elif point == '3':
        print('Введіть перший множник: ', end='')
        num1 = number()
        print('Введіть другий множник: ', end='')
        num2 = number()
        result = num1 * num2
        print(f'Добуток: {result}')
    elif point == '4':
        print('Введіть ділене: ', end='')
        num1 = number()
        print('Введіть дільник: ', end='')
        num2 = number()
        try:
            result = num1 // num2
        except ZeroDivisionError:
            result = 'infinity'
        print(f'Частка: {result}')
    elif point == '5':
        print('Введіть число: ', end='')
        num1 = number()
        print('Введіть степінь: ', end='')
        num2 = number()
        result = num1 ** num2
        print(f'Результат: {result}')
    elif point == '6':
        print('Введіть число: ', end='')
        num1 = number()
        print('Введіть степінь кореня: ', end='')
        num2 = number()
        result = num1 ** (1 / num2)
        print(f'Результат: {result}')
    elif point == '7':
        def sub_number():
            while True:
                num = number()
                if num < 0:
                    print('Процент не може бути мінусовий')
                else:
                    return num
                    break


        print('Введіть число: ', end='')
        num1 = number()
        print('Введіть відсотки: ', end='')
        num2 = sub_number()
        result = num1 * (num2 / 100)
        print(f'Результат: {result}')
    elif point == '8':
        break
    else:
        print('Incorrect!')
