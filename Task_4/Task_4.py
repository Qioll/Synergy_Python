# -*- coding: cp1251 -*-

print(f'������� �1:')

print("������� ������� ��������������:")
width = float(input("������: "))
height = float(input("������: "))

area = width * height
perimeter = 2 * (width + height)

print(f"������� �������������� ����� {area}")
print(f"�������� �������������� ����� {perimeter}")

print(f'������� �2:')

number = int(input("������� ����������� �����: "))

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

result = (tens ** ones) * hundreds / (ten_thousands - thousands)

print("���������:", result)

