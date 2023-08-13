# -*- coding: cp1251 -*-

print('������� �1')

pets = {}

pet_name = input("������� ��� �������: ")
pet_type = input("������� ��� �������: ")
pet_age = int(input("������� ������� �������: "))
owner_name = input("������� ��� ���������: ")

pets[pet_name] = {
    "��� �������": pet_type,
    "������� �������": pet_age,
    "��� ���������": owner_name
}

for pet_name, pet in pets.items():
    pet_type = pet["��� �������"]
    pet_age = pet["������� �������"]
    owner_name = pet["��� ���������"]

    if pet_age % 10 == 1 and pet_age % 100 != 11:
        age_word = "���"
    elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
        age_word = "����"
    else:
        age_word = "���"

print(f'��� {pet_type.lower()} �� ������ "{pet_name}". ������� �������: {pet_age} {age_word}. ��� ���������: {owner_name}')

print('������� �2')

start = int(input("������� ��������� ��������: "))
end = int(input("������� �������� ��������: "))

my_dict = {}

if start < end:
    step = 1
else:
    step = -1

for i in range(start, end + step, step):
    my_dict[i] = i ** i

print("���������:")
for key, value in my_dict.items():
    print(key, ":", value)