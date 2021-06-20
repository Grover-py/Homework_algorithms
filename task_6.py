# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

my_list = [43, -81, -16, -21, 27, 14, 39, 50, 0, 14, 18, -3, -3, 8, -2]

x = my_list.index(min(my_list))
y = my_list.index(max(my_list))

if x > y:
    x, y = y, x

answer = 0

for el in range(len(my_list)):
    if x < el < y:
        answer += my_list[el]

print(answer)
