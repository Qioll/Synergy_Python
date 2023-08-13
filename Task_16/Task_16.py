# -*- coding: UTF_8 -*-

print('Задание №1')

class CashRegister:
    def __init__(self, money):
        self.money = money

    def top_up(self, amount):
        self.money += amount

    def count_1000(self):
        thousands = self.money // 1000
        return thousands

    def take_away(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            raise ValueError("Недостаточно денег в кассе")

register = CashRegister(5000) # создаем объект класса CashRegister с начальным количеством денег 5000

print(register.count_1000()) # выводим количество целых тысяч в кассе (5)

register.top_up(2000) # пополняем кассу на 2000

print(register.count_1000()) # выводим обновленное количество целых тысяч в кассе (7)

register.take_away(3000) # забираем из кассы 3000

print(register.count_1000()) # выводим обновленное количество целых тысяч в кассе (4)


print('Задание №2')


class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("s не может быть меньше или равно 0")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        if dx % self.s + dy % self.s == 0:
            return dx // self.s + dy // self.s
        print(
            f"Точка ({x2}, {y2}) недостижима из точки ({self.x}, {self.y}) с шагом {self.s}"
        )
        return None


turtle = Turtle(0, 0, 1)
turtle.go_up()
turtle.go_right()
turtle.evolve()
turtle.go_up()
turtle.count_moves(3, 4)
turtle.degrade()
turtle.go_right()
turtle.go_right()
turtle.count_moves(5, 2)