# -*- coding: UTF_8 -*-

print(f'Задание №1:')

print("Введите размеры прямоугольника:")
width = float(input("Ширина: "))
height = float(input("Высота: "))

area = width * height
perimeter = 2 * (width + height)

print(f"Площадь прямоугольника равна {area}")
print(f"Периметр прямоугольника равен {perimeter}")

print(f'Задание №2:')

number = int(input("Введите пятизначное число: "))

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

result = (tens ** ones) * hundreds / (ten_thousands - thousands)

print("Результат:", result)

