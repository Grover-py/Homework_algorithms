# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random as rd

my_list = []
my_list_2 = []

for el in range(10):
    my_list.append(rd.randint(1, 11))

for el in range(len(my_list)):
    if my_list[el] % 2 == 0:
        my_list_2.append(el)

print(my_list)
print(my_list_2)
