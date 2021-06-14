# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.

import time
dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

int_list = []


question = int(input('\nЧто будем генерировать? Случайное целое число (1),\n'
                     'Случайное вещественное число (2),\n'
                     'Случайный символ (3)\n\n'
                     'Введи цифру, 1, 2 или 3: '))

start = input('\nВведи начало диапазона: ')
end = input('\nВведи конец диапазона: ')

if question == 1:
    start, end = int(start), int(end)
    if end < start:
        start, end = end, start
    while start <= end:
        int_list.append(start)
        start += 1
elif question == 2:
    start, end = float(start), float(end)
    if end < start:
        start, end = end, start
    while start <= end:
        int_list.append(round(start, 3))
        start += 0.05
    if not end in int_list:
        int_list.append(end)
elif question == 3:
    start, end = dictionary.index(start.lower()), dictionary.index(end.lower())
    if end < start:
        start, end = end, start
    while start <= end:
        int_list.append(dictionary[start])
        start += 1

print(int_list[int(round(time.time() % len(int_list) - 1, 0))])