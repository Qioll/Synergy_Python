# -*- coding: cp1251 -*-

print('������� �1')

N = int(input("������� ���������� �����: "))

numbers = list(map(int, input("������� ����� ����� ������: ").split()))

distinct_numbers = len(set(numbers))

print("���������� ��������� �����:", distinct_numbers)

print('������� �2')

list1 = list(map(int, input("������� ����� ������� ������ ����� ������: ").split()))

list2 = list(map(int, input("������� ����� ������� ������ ����� ������: ").split()))

common_numbers = len(set(list1) & set(list2))

print("���������� �����, ������������ ������������ � ����� �������:", common_numbers)

print('������� �3')

numbers = input("������� ������������������ ����� ����� ������: ").split()

unique_numbers = set()

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.add(num)
        print("NO")
    else:
        print("YES")
