import sys

def func_1(x):
    print(f'Программа занимает: 0 байт')
    return str(x)[::-1]

def func_2(x):
    my_str = ''
    for el in str(x)[::-1]:
        my_str += el
    print(f'Программа занимает: {sys.getsizeof(my_str) + sys.getsizeof(el)} байт')
    return my_str

def func_3(x):
    my_list = [el for el in str(x)]
    my_str = ''
    for el in range(len(my_list)):
        my_str += my_list.pop()
    print(f'Программа занимает: {sys.getsizeof(my_list) + sys.getsizeof(my_str) + sys.getsizeof(el)} байт')
    return my_str


print(func_1(123450))
print(func_2(123450))
print(func_3(123450))