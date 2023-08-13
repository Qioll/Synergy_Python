# -*- coding: cp1251 -*-

print("������� �1")

number = int(input("������� �����: "))

description = ""
if number < 0:
    description = "�������������"
elif number == 0:
    description = "�������"
else:
    description = "�������������"

if number % 2 == 0:
    description += " ������"
else:
    description += " ��������"
    print("����� �� �������� ������")

print(f"{description} �����")

print('������� �2')

word = input("������� �����: ")
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

print("�������:")
for vowel in vowels:
    if vowel in letter_count:
        vowel_count += letter_count[vowel]
        print(vowel, ":", letter_count[vowel])
    else:
        print(vowel, ": False")

print("���������:")
for letter in letter_count:
    if letter not in vowels:
        consonant_count += letter_count[letter]
        print(letter, ":", letter_count[letter])

if vowel_count > 0 and consonant_count > 0:
    print("���������� �������:", vowel_count)
    print("���������� ���������:", consonant_count)
else:
    print(False)

print('������� �3')

X = int(input("������� ����������� ����� ����������: "))
A = int(input("������� ����� ����� � ������: "))
B = int(input("������� ����� ����� � �����: "))

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