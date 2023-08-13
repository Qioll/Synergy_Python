# -*- coding: UTF_8 -*-

print('Задание №1')

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

autobus = Autobus("Renaul Logan", 180, 12)
print("Название автомобиля:", autobus.name, "Скорость:", autobus.max_speed, "Пробег:", autobus.mileage)

print('Задание №2')

class Transport_new:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


class Autobus_new(Transport_new):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


autobus = Autobus_new("Renaul Logan", 180, 12)
print(autobus.seating_capacity())


