# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.

n = int(input("Input any number: "))
k = 1
while k <= n:
    print(k, end=' ')
    k *= 2