# -*- coding: UTF_8 -*-

print("Задание №1")

number = int(input("Введите число: "))

description = ""
if number < 0:
    description = "отрицательное"
elif number == 0:
    description = "нулевое"
else:
    description = "положительное"

if number % 2 == 0:
    description += " четное"
else:
    description += " нечетное"
    print("Число не является четным")

print(f"{description} число")

print('Задание №2')

word = input("Введите слово: ")
vowels = {'a', 'e', 'i', 'o', 'u'}

letter_count = {}

for letter in word:
    if letter.isalpha():
        letter = letter.lower()
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

vowel_count = 0
consonant_count = 0

print("Гласные:")
for vowel in vowels:
    if vowel in letter_count:
        vowel_count += letter_count[vowel]
        print(vowel, ":", letter_count[vowel])
    else:
        print(vowel, ": False")

print("Согласные:")
for letter in letter_count:
    if letter not in vowels:
        consonant_count += letter_count[letter]
        print(letter, ":", letter_count[letter])

if vowel_count > 0 and consonant_count > 0:
    print("Количество гласных:", vowel_count)
    print("Количество согласных:", consonant_count)
else:
    print(False)

print('Задание №3')

X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Введите сумму денег у Майкла: "))
B = int(input("Введите сумму денег у Ивана: "))

if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)