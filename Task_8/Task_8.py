# -*- coding: UTF_8 -*-

print('Задание №1')

n = int(input("Введите количество чисел: "))
nums = []
for i in range(n):
    num = int(input("Введите число {}/{}: ".format(i+1, n)))
    nums.append(num)

reversed_nums = nums[::-1]
print("Перевернутый массив чисел:")
for num in reversed_nums:
    print(num)

    
print('Задание №2')

n = int(input("Введите количество чисел: "))

array = list(map(int, input("Введите {} чисел через пробел: ".format(n)).split()))

if n != len(array):
    print("Ошибка: количество чисел не соответствует введенному значению N.")
else:
    modified_array = []

    for i in range(n - 1, -1, -1):
        modified_array.append(array[i])

    print("Измененный массив:")
    print(' '.join(map(str, modified_array)))

    
print('Задание №3')

m = int(input("Введите максимальную массу, которую может выдержать одна лодка: "))


n = int(input("Введите количество рыбаков: "))

weights = [] 

for i in range(n):
    weight = int(input(f"Введите вес рыбака #{i+1}: "))
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
print("Минимальное количество лодок, необходимое для переправки всех рыбаков:", count)