# -*- coding: UTF_8 -*-

print('Задание №1')

N = int(input("Введите количество чисел: "))

numbers = list(map(int, input("Введите числа через пробел: ").split()))

distinct_numbers = len(set(numbers))

print("Количество различных чисел:", distinct_numbers)

print('Задание №2')

list1 = list(map(int, input("Введите числа первого списка через пробел: ").split()))

list2 = list(map(int, input("Введите числа второго списка через пробел: ").split()))

common_numbers = len(set(list1) & set(list2))

print("Количество чисел, содержащихся одновременно в обоих списках:", common_numbers)

print('Задание №3')

numbers = input("Введите последовательность чисел через пробел: ").split()

unique_numbers = set()

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.add(num)
        print("NO")
    else:
        print("YES")
