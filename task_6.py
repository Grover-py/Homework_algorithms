# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

num_user = int(input('Введите номер буквы в алфавите: '))
letter_user = dictionary[num_user - 1]

print(f'Под номером: {num_user}, в алфивите находится буква: {letter_user}')