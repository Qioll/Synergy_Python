# -*- coding: cp1251 -*-

print('������� �1')

n = int(input("������� ���������� �����: "))
nums = []
for i in range(n):
    num = int(input("������� ����� {}/{}: ".format(i+1, n)))
    nums.append(num)

reversed_nums = nums[::-1]
print("������������ ������ �����:")
for num in reversed_nums:
    print(num)

    
print('������� �2')

n = int(input("������� ���������� �����: "))

array = list(map(int, input("������� {} ����� ����� ������: ".format(n)).split()))

if n != len(array):
    print("������: ���������� ����� �� ������������� ���������� �������� N.")
else:
    modified_array = []

    for i in range(n - 1, -1, -1):
        modified_array.append(array[i])

    print("���������� ������:")
    print(' '.join(map(str, modified_array)))

    
print('������� �3')

m = int(input("������� ������������ �����, ������� ����� ��������� ���� �����: "))


n = int(input("������� ���������� �������: "))

weights = [] 

for i in range(n):
    weight = int(input(f"������� ��� ������ #{i+1}: "))
    weights.append(weight)

weights.sort()  
i = 0
j = n - 1
count = 0
while i <= j:
    if weights[j] + weights[i] <= m:
        i += 1
    j -= 1
    count += 1
print("����������� ���������� �����, ����������� ��� ���������� ���� �������:", count)