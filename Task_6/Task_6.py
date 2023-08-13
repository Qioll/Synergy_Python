# -*- coding: UTF_8 -*-

print('Задание №1')

n = int(input("Введите количество чисел: "))  

count = 0  

for i in range(n):
    num = int(input("Введите число: "))  
    if num == 0: 
        count += 1

print("Количество чисел равных нулю: ", count) 

print('Задание №2')

x = int(input("Введите натуральное число: "))
count = 0
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        count += 1
        if x // i != i:
            count += 1
print("Количество натуральных делителей числа", x, ":", count)

num_A = int(input("Введите число A: "))
num_B = int(input("Введите число B: "))

print('Задание №2')

if num_A > num_B:
    num_A, num_B = num_B, num_A

for num in range(num_A, num_B + 1):
    if num % 2 == 0:
        print(num, end=" ")