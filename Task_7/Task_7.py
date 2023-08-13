# -*- coding: cp1251 -*-

print('Задание №1')

s = input("Введите строку без пробелов: ")
if s == s[::-1]:
    print("Yes")
else:
    print("No")

print('Задание №2')

string = input("Введите строку: ")
new_string = " ".join(string.split())

print("Преобразованная строка:", new_string)