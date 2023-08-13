# -*- coding: cp1251 -*-

print('Задание №1')

print('Введите данные питомца:')
kind = input('Вид: ')
age = input('Возраст: ')
name = input('Кличка: ')

print('Это {} по кличке "{}". Возраст: {} года.'.format(kind, name, age))

print('Задание №2')

print('Введите 11 стадий эволюции человека:')
stages = [input() for _ in range(11)]

print('Ваш ответ:', end=' ')
print(' => '.join(stages))
