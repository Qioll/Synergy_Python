# -*- coding: cp1251 -*-

print('������� �1')

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

autobus = Autobus("Renaul Logan", 180, 12)
print("�������� ����������:", autobus.name, "��������:", autobus.max_speed, "������:", autobus.mileage)

print('������� �2')

class Transport_new:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"�������� ����������: {self.name} ��������: {self.max_speed} ������: {self.mileage}"

    def seating_capacity(self, capacity):
        return f"����������� ������ �������� {self.name}: {capacity} ����������"


class Autobus_new(Transport_new):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


autobus = Autobus_new("Renaul Logan", 180, 12)
print(autobus.seating_capacity())


