# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.

print(bin(5))
print(bin(6))
print(bin(5 & 6))
print(int(bin(5 & 6), 2))

print(bin(5 | 6))
print(int(bin(5 | 6), 2))

print(bin(5 ^ 6))
print(int(bin(5 ^ 6), 2))

print(bin(5 >> 2))
print(int(bin(5 >> 2), 2))
print(bin(5 << 2))
print(int(bin(5 << 2), 2))