# -*- coding: cp1251 -*-

print('������� �1')

print('������� ������ �������:')
kind = input('���: ')
age = input('�������: ')
name = input('������: ')

print('��� {} �� ������ "{}". �������: {} ����.'.format(kind, name, age))

print('������� �2')

print('������� 11 ������ �������� ��������:')
stages = [input() for _ in range(11)]

print('��� �����:', end=' ')
print(' => '.join(stages))
