# -*- coding: cp1251 -*-

import random

matrix1 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(-50, 50))
    matrix1.append(row)

matrix2 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(-50, 50))
    matrix2.append(row)

matrix3 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row)

print("������ �������:")
for row in matrix1:
    print(row)

print("\n")

print("������ �������:")
for row in matrix2:
    print(row)

print("\n")

print("������ ������� (����� ������ � ������ ������):")
for row in matrix3:
    print(row)
