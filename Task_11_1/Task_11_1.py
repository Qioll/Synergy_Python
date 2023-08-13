# -*- coding: cp1251 -*-

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_list(f):
    result = []
    for i in range(f, 0, -1):
        result.append(factorial(i))
    return result


n = int(input('������� �����: '))
f = factorial(n)
print(f'��������� {n} ����� {f}')
print(factorial_list(f))
