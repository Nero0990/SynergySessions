"""
Задание Nº1
Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
• top_up(X) - пополнить на Х
• count_10000 - выводит сколько целых тысяч осталось в кассе
• take_away(X) - забрать Х из кассы, либо выкинуть ошибку, что не достаточно денег
"""


class Касса:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def top_up(self, X):
        self.amount += X

    def count_10000(self):
        return self.amount // 10000

    def take_away(self, X):
        if X > self.amount:
            raise ValueError("Недостаточно денег в кассе")
        self.amount -= X


касса = Касса(50000)
касса.top_up(15000)
print(f"Сколько целых тысяч осталось в кассе: {касса.count_10000()}")
касса.take_away(20000)
print(f"Сколько целых тысяч осталось в кассе: {касса.count_10000()}")
