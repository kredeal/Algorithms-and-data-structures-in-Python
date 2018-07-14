# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

print('\nГенерируем случайное целое число !')
x, y = input('Введите диапазон для генерации числа (два числа через запятую) : ').split(',')
if x < y:
    print(random.randrange(int(x), int(y)))
if y < x:
    print(random.randrange(int(y), int(x)))
if x == y:
    print('Не верный диапазон!')

print('\nГенерируем случайное вещественное число !')
x, y = input('Введите диапазон для генерации числа (два числа через запятую) : ').split(',')
if x < y:
    print(random.uniform(float(x), float(y)))
if y < x:
    print(random.uniform(float(y), float(x)))
if x == y:
    print('Не верный диапазон!')

print('\nГенерируем случайный символ английского алфавита!')
letter1, letter2 = input(
    'Введите диапазон для генерации символа (две строчные буквы английского алфавита через запятую) : ').split(',')
if ord(letter1) < ord(letter2):
    print(chr(random.randint(ord(letter1), ord(letter2))))
if ord(letter2) < ord(letter1):
    print(chr(random.randint(ord(letter2), ord(letter1))))
if ord(letter1) == ord(letter2):
    print('Не верный диапазон! ')
