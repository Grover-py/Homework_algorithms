# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

a = [[4, 5, 7], [5, 2, 8], [9, 6, 5], [1, 8, 7]]

for el in range(len(a)):
    for i in range(len(a[el])):
        print("%4d" % a[el][i], end="")
    print()

answer = min(min(a))

for el in range(len(a[0])):
    x = max(max(a))
    for i in range(len(a)):
        if a[i][el] <= x:
            x = a[i][el]
    if x > answer:
        answer = x

print(answer)