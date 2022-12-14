import run_game
from figure import *


class Tetris:
    score = 0
    state = "НАЧАТЬ"
    field = []
    n2 = 0
    n1 = 0
    x = 20
    y = 20
    zoom = 40
    figure = None
#сетка(поле)
    def __init__(self, n2, n1):
        self.n2 = n2
        self.n1 = n1
        self.field = []
        self.score = 0
        self.state = "НАЧАТЬ"
        for i in range(n2):
            new_line = []
            for j in range(n1):
                new_line.append(0)
            self.field.append(new_line)
#новая фигурка
    def new_figure(self):
        self.figure = Figure(3, 0)
#непересечения
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.n2 - 1 or \
                            j + self.figure.x > self.n1 - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection
#подсчет очков
    def break_lines(self):
        lines = 0
        for i in range(1, self.n2):
            zeros = 0
            for j in range(self.n1):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.n1):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2
#пространство между фигурками или его отсутствие
    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()
#движение вниз
    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()
#достижение верхушки игрового поля
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "ИГРА ОКОНЧЕНА"
#движение вбок
    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x
#повороты фигурки
    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation