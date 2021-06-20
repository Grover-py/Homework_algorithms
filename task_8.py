# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

string_1 = [int(el) for el in input('Введите первую строку матрицы: ').split()]
string_2 = [int(el) for el in input('Введите вторую строку матрицы: ').split()]
string_3 = [int(el) for el in input('Введите третью строку матрицы: ').split()]
string_4 = [int(el) for el in input('Введите четвёртую строку матрицы: ').split()]

a = [string_1, string_2, string_3, string_4]

for el in range(len(a)):
    for i in range(len(a[el])):
        print("%4d" % a[el][i], end="")
    print("%4d" % sum(a[el]))