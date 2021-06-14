# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num_1 = int(input('Введите первую цифру: '))
num_2 = int(input('Введите вторую цифру: '))
num_3 = int(input('Введите третью цифру: '))

sum_user = num_1 + num_2 + num_3
composition_usr = num_1 * num_2 * num_3

print(f'Сумма, Ваших, чисел равняется: {sum_user}, а произведение: {composition_usr}')