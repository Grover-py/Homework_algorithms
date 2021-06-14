# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

in_letter_1 = input('Пожалуйста введите первую букву: ')
in_letter_2 = input('Пожалуйста введите вторую букву: ')

index_letter_1 = dictionary.index(in_letter_1) + 1
index_letter_2 = dictionary.index(in_letter_2) + 1
interval = dictionary.index(in_letter_2) - dictionary.index(in_letter_1) - 1

print(f'Первая буква алфавита стоит на месте №: {index_letter_1}, а вторая буква стоит на месте №: '
      f'{index_letter_2}, букв между ними: {interval}')