import pygame
from pygame.draw import circle
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''рисует новый шарик '''
    global x, y, z
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

    #сюда добавить словарь с координатами и скоростями 


def click(event):
    print(x, y, r)


def print_screen()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
balls = [new_ball() for _ in range(10)]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = pygame.mouse.get_pos()
            for i, ball in enumerate(balls):
                if (((ball['x'] - x1) ** 2 + (ball['y'] - y1) ** 2) ** (1 / 2)) <= balls['r']:
                    balls[i] = new_ball()
                    print_screen("yay!")
                    n += 1

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()
