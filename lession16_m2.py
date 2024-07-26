"""
Задание № 2
Создайте класс Черепашка, который хранит позиции х и у черепашки, 
а также s - количество клеточек, на которое она перемещается за ход
у этого класс есть методы:
• go_up - увеличивает у на s
• go_down() - уменьшает у на s
• go_left - уменьшает х на s
• go_rightO - увеличивает у на s
• evolve() - увеличивает s на 1
• degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
• count_moves(x2, y2) - возвращает минимальное количество действий, 
за которое черепашка сможет добраться до х2 у2 от текущей позиции"""


class Turtle:
    def __init__(self, x=0, y=0, s=1):
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
        return (dx + dy) // self.s


turtle = Turtle()
turtle.go_up()
turtle.go_right()
turtle.evolve()
print(f"Текущая позиция: ({turtle.x}, {turtle.y}), размер шага: {turtle.s}")
moves = turtle.count_moves(10, 10)
print(f"Минимальное количество ходов до (10, 10): {moves}")
