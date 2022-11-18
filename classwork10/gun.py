import math
from random import choice
import random
import pygame
from pygame.draw import *


FPS = 30

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GREY = (138, 127, 142)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

g = 0.7 # ускорение св падения
mu = 0.85 # затухание при ударе
a1 = 10 # стенки
a2 = 20

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ параметры шара"""
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """перемещение шара за один кадр перерисовки"""
        self.x += self.vx
        self.y += self.vy
        self.vy += g
        if (self.x > WIDTH - a1 - self.r) or (self.x < a1 + self.r):
            self.vy = mu * self.vy
            self.vx = - mu * self.vx
            self.vy = mu * self.vy
        if (self.y > HEIGHT - a2 - self.r) or (self.y < a2 + self.r):
            self.vy = - mu * self.vy
            self.vx = mu * self.vx

    def draw(self):
        """рисование шара"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """столкновение с мишенью """
        if ((obj.x - self.x) **2  + (obj.y - self.y)**2 <= (self.r + obj.r) ** 2):
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        """задаются параметры пушки"""
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.x = 70
        self.y = 450
        self.l = 10
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание (в направлении мыши)"""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """рисуется пушка"""
        polygon(self.screen, self.color, [(self.x - math.sin(self.an) * self.l, self.y + math.cos(self.an) * self.l), (self.x + math.sin(self.an) * self.l, self.y - math.cos(self.an)*self.l), (self.x + math.sin(self.an) * self.l + math.cos(self.an) * self.f2_power, self.y - math.cos(self.an) * self.l + math.sin(self.an) * self.f2_power), (self.x - math.sin(self.an) * self.l + math.cos(self.an) * self.f2_power, self.y + math.cos(self.an) * self.l + math.sin(self.an) * self.f2_power)])

    def power_up(self):
        """сила выстрела пушки(задает начальную скорость)"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """создается мишень"""
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(5, 50)
        self.vx = random.randint(0, 20)
        self.vy = random.randint(0, 20)
        self.color = choice(GAME_COLORS)
        self.points = 0
        self.live = 1

    def new_target(self):
        """ Инициализация новой мишени"""
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(5, 50)
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)
        self.color = choice(GAME_COLORS)
        self.points = 0
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в мишень """
        self.points += points

    def draw(self):
        """форма шарика """
        circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """движение шариков """
        self.x += self.vx
        self.y += self.vy
        self.vy += random.randint(-1, 1)
        self.vx += random.randint(-1, 1)
        if (self.x > WIDTH - a1 - self.r) or (self.x < a1 + self.r):
            self.vy = mu * self.vy
            self.vx = - mu * self.vx
            self.vy = mu * self.vy
        if (self.y > HEIGHT - a2 - self.r) or (self.y < a2 + self.r):
            self.vy = - mu * self.vy
            self.vx = mu * self.vx

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bullet = 0
balls = []
clock = pygame.time.Clock()
gun = Gun(screen)
target_1 = Target()
target_2 = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target_1.draw()
    target_2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if (b.hittest(target_1)) and (target_1.live):
            target_1.live = 0
            target_1.hit()
            target_1.new_target()
        if (b.hittest(target_2)) and (target_2.live):
            target_2.live = 0
            target_2.hit()
            target_2.new_target()
    target_1.move()
    target_2.move()
    gun.power_up()

pygame.quit()