# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = input('Введите три числа через запятую: ').split(',')

a = int(a)
b = int(b)
c = int(c)

if b < a < c or c < a < b:
    print('{} среднее число'.format(a))
if a < b < c or c < b < a:
    print('{} среднее число'.format(b))
if a < c < b or b < c < a:
    print('{} среднее число'.format(c))
