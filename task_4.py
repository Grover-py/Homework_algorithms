# 4. Определить, какое число в массиве встречается чаще всего.

my_list = [2, 4, 11, 12, 5, 11, 5, 4, 11, 3]

x = 0
answer = None

for el in my_list:
    n = 0
    for i in my_list:
        if el == i:
            n += 1
    if n > x:
        x = n
        answer = el


print(f'Чаще всего (аж {x} раза) встречается число: {answer}')
