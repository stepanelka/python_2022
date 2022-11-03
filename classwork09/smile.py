import pygame
from pygame.draw import circle, polygon, rect


pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

#colors
yellow = (255, 240, 0)
red = (255, 31, 0)
black = (0, 0, 0)

#circle
circle(screen, yellow, (300, 300), 200)
#eyes
circle(screen, red, (240, 250), 40)
circle(screen, red, (360, 250), 35)
circle(screen, black, (300, 300), 200, 2)
circle(screen, black, (240, 250), 40, 2)
circle(screen, black, (360, 250), 35, 2)
circle(screen, black, (240, 250), 20)
circle(screen, black, (360, 250), 20)

#eyebrows
polygon(screen, black, [(250, 200), (260, 220), (200, 150), (210, 140)])
polygon(screen, black, [(350, 200), (340, 220), (400, 150), (390, 140)])

#background
rect(screen, black, (225, 400, 150, 30))





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
