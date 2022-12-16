import pygame.mouse
import pygame
from pygame.draw import *
from pygame.mixer import *
from Sounds import *
from parametry import *
from tetris import *
import run_game



#задание и работа с кнопками
class Button:
    #ширина, высота кнопки, цвета при наведении и без
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (221, 213, 254)
        self.active_color = (159, 140, 251)
    #рисование кнопок, нажатие и наведение на них
    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            rect(screen, self.active_color, (x, y, self.width, self.height))
            if click[0] == 1 and run_game.game.state == "НАЧАТЬ":
                Sound.play(button_sound)
                pygame.time.delay(300)
                if action is not None:
                    if action == exit:
                        exit()
                    elif action == "ПРОДОЛЖИТЬ":
                        run_game.pause = False
                    elif action == "ЗАНОВО":
                        run_game.rgame = False
                        run_game.game.state = "НАЧАТЬ"
                    else:
                         action()
                else:
                    return True
        else:
            rect(screen, self.inactive_color, (x, y, self.width, self.height))

        screen.blit(message, (x, y - 5))