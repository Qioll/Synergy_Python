# -*- coding: cp1251 -*-

print('������� �1')

s = input("������� ������ ��� ��������: ")
if s == s[::-1]:
    print("Yes")
else:
    print("No")

print('������� �2')

string = input("������� ������: ")
new_string = " ".join(string.split())

print("��������������� ������:", new_string)