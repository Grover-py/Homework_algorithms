from collections import namedtuple, deque

all_comp = []
Company = namedtuple('Company', ['name', 'profit'])

n = int(input('Введите количество организаций: '))
total_profit = 0

for el in range(n):
    name = input('Введите имя организации: ')
    profit_by_quarter = []
    for i in range(1, 5):
        profit_by_quarter.append(int(input(f'Прибыль за квартал №: {i} - ')))
    total_profit += sum(profit_by_quarter)
    all_comp.append(Company(name=name, profit=sum(profit_by_quarter)))

average = total_profit / n

less_profit = []
more_profit = []

for comp in all_comp:
    if comp.profit > average:
        more_profit.append(comp.name)
    else:
        less_profit.append(comp.name)


print(f'Компании, чья прибыль выше среднего: {more_profit}\nКомпании, чья прибль ниже среднего: {less_profit}\n')