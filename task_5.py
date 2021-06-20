# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

my_list = [43, -8, -16, -21, -27, 14, -39, 50, 0, 14, 18, -3, -3, 8, -2]

answer = 0

for el in my_list:
    if el < answer:
        answer = el

for el in my_list:
    if answer < el < 0:
        answer = el


print(f'Максимальный отрицательный элемент: {answer}')
print(f'Его позиция в массиве: {my_list.index(answer) + 1}')