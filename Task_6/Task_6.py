# -*- coding: cp1251 -*-

print('������� �1')

n = int(input("������� ���������� �����: "))  

count = 0  

for i in range(n):
    num = int(input("������� �����: "))  
    if num == 0: 
        count += 1

print("���������� ����� ������ ����: ", count) 

print('������� �2')

x = int(input("������� ����������� �����: "))
count = 0
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        count += 1
        if x // i != i:
            count += 1
print("���������� ����������� ��������� �����", x, ":", count)

num_A = int(input("������� ����� A: "))
num_B = int(input("������� ����� B: "))

print('������� �2')

if num_A > num_B:
    num_A, num_B = num_B, num_A

for num in range(num_A, num_B + 1):
    if num % 2 == 0:
        print(num, end=" ")