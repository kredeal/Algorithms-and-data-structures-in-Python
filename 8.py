# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год: '))

if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 != 0:
            print('{} год високосный!'.format(year))
    else:
        print('{} год високосный!'.format(year))
else:
    print('{} год не високосный!'.format(year))
