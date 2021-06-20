# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

my_list = [2, 4, 11, 11, 12, 5, 5, 4, 11, 3]
print(my_list)

x = my_list.index(max(my_list))
y = my_list.index(min(my_list))

my_list[x], my_list[y] = my_list[y] , my_list[x]

print(my_list)