# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

sequence_num = list(input('Введите последовательность чисел через пробел: ').split(' '))
max_num = 0
max_sum = 0


for el in sequence_num:
    x = 0
    for i in str(el):
        x += int(i)
    if x > max_sum:
        max_num = el
        max_sum = x

print(f'Наибольшее по сумме цифр число: {max_num}. Сумма его цифр: {max_sum}')