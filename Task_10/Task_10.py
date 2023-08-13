# -*- coding: cp1251 -*-

print('Задание №1')

pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

for pet_name, pet in pets.items():
    pet_type = pet["Вид питомца"]
    pet_age = pet["Возраст питомца"]
    owner_name = pet["Имя владельца"]

    if pet_age % 10 == 1 and pet_age % 100 != 11:
        age_word = "год"
    elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
        age_word = "года"
    else:
        age_word = "лет"

print(f'Это {pet_type.lower()} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}')

print('Задание №2')

start = int(input("Введите начальное значение: "))
end = int(input("Введите конечное значение: "))

my_dict = {}

if start < end:
    step = 1
else:
    step = -1

for i in range(start, end + step, step):
    my_dict[i] = i ** i

print("Результат:")
for key, value in my_dict.items():
    print(key, ":", value)