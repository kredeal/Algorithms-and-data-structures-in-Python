# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import math

letter1, letter2 = input(
    'Введите диапазон букв (две строчные буквы английского алфавита через запятую) : ').split(',')

number1 = ord(letter1) - 96
number2 = ord(letter2) - 96

print('Первая буква имеет номер {} в английском алфавите\n'
      'Вторая буква имеет номер {} в английском алфавите\n'
      'Количество букв между ними = {}'.format(number1, number2, abs(number1 - number2) - 1))
Q = input('Хотите посмотреть эти буквы? Если да, нажмите в английской раскладке "y" и "Enter" : ')
if Q == 'y':
    if ord(letter1) < ord(letter2):
        for i in range(ord(letter1)+1,ord(letter2)):
            print('{}, '.format(chr(i)), end="")
    elif ord(letter1) > ord(letter2):
        for i in range(ord(letter2)+1,ord(letter1)):
            print('{}, '.format(chr(i)), end="")

