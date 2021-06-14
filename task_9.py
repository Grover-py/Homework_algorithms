# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = int(input('Введите число № 1: '))
num_2 = int(input('Введите число № 2: '))
num_3 = int(input('Введите число № 3: '))

a = num_1

if num_1 < num_2 < num_3 or num_1 > num_2 > num_3:
    a = num_2
elif num_1 < num_3 < num_2 or num_1 > num_3 > num_2:
    a = num_3

print(a)
