# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

my_list = [1, 2, 3, 4, 0]


answer_1 = min(my_list)
my_list_2 = []
for el in range(len(my_list)):
    if el != my_list.index(answer_1):
        my_list_2.append(my_list[el])

answer_2 = min(my_list_2)


print(answer_1)
print(answer_2)