# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

my_list = [el for el in range(2, 100)]

multiple_of_2 = 0
multiple_of_9 = 0

for el in my_list:
    if el % 2 == 0:
        multiple_of_2 += 1
    elif el % 9 == 0:
        multiple_of_9 += 1

print(f'{multiple_of_2 = }')
print(f'{multiple_of_9 = }')