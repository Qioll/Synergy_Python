# -*- coding: cp1251 -*-

import collections

pets = {
    1: {
        "������": {
            "��� �������": "������",
            "������� �������": 9,
            "��� ���������": "�����",
        },
    },
    2: {
        "���": {
            "��� �������": "���������� �����",
            "������� �������": 19,
            "��� ���������": "����",
        },
    },
}


def get_pet(id):
    return pets[id] if id in pets.keys() else False


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "���"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "����"
    else:
        return "���"


def pets_list():
    for id in pets:
        pet = get_pet(id)
        name = list(pet.keys())[0]
        info = pet[name]
        type = info["��� �������"]
        age = info["������� �������"]
        owner = info["��� ���������"]
        print(
            f'ID: {id}. ��� {type} �� ������ "{name}". ������� �������: {age} {get_suffix(age)}. ��� ���������: {owner}'
        )


def create(name, pet_type, age, owner):
    last = collections.deque(pets, maxlen=1)[0]
    id = last + 1
    pets[id] = {
        name: {"��� �������": pet_type, "������� �������": age, "��� ���������": owner}
    }


def read(id):
    pet = get_pet(id)
    if pet:
        name = list(pet.keys())[0]
        info = pet[name]
        age = info["������� �������"]
        owner = info["��� ���������"]
        type = info["��� �������"]
        print(
            f'��� {type} �� ������ "{name}". ������� �������: {age} {get_suffix(age)}. ��� ���������: {owner}'
        )
        return True
    print(f"������! ID={id} ����������� � ����")
    return False


def update(id, name=None, type=None, age=None, owner=None):
    pet = get_pet(id)
    if pet:
        name = list(pet.keys())[0]
        if name is not None:
            pet = {name: pet[name]}
            name = name
        if type is not None:
            pet[name]["��� �������"] = type
        if age is not None:
            pet[name]["������� �������"] = age
        if owner is not None:
            pet[name]["��� ���������"] = owner

        pets[id] = pet
        return True
    print(f"������! ID={id} ����������� � ����")
    return False


def delete(id):
    if id in pets:
        del pets[id]
        return True
    print(f"������! ID={id} ����������� � ����")
    return False


command = ""
while command != "stop":
    command = input("������� ������� (create/read/update/delete/stop): ")
    if command == "create":
        name = input("������� ��� �������: ")
        type = input("������� ��� �������: ")
        age = int(input("������� ������� �������: "))
        owner = input("������� ��� ���������: ")
        create(name, type, age, owner)
    elif command == "read":
        id = int(input("������� ������������� �������: "))
        read(id)
    elif command == "update":
        id = int(input("������� ������������� �������: "))
        if read(id):
            name = input(
                "������� ����� ��� ������� (�������� ������, ���� �� ������ ������): "
            )
            name = name if name else None
            type = input(
                "������� ����� ��� ������� (�������� ������, ���� �� ������ ������): "
            )
            type = type if type else None
            age = input(
                "������� ����� ������� ������� (�������� ������, ���� �� ������ ������): "
            )
            age = int(age) if age else None
            owner = input(
                "������� ����� ��� ��������� (�������� ������, ���� �� ������ ������): "
            )
            owner = owner if owner else None
            update(id, name, type, age, owner)
    elif command == "delete":
        id = int(input("������� ������������� �������: "))
        delete(id)
    elif command == "stop":
        break
    else:
        print("����������� �������")