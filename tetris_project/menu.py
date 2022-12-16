import pygame
import Img
import parametry as p
from button import *
import run_game
from states import *


#начальное меню
def show_menu():

    start_button = Button(345, 100)
    quit_button = Button(345, 100)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        p.screen.blit(Img.bg_menu, (0, 0))
        if start_button.draw(175, 250, title_start):
            run_game.game_state.change(State.START)
            return
        if quit_button.draw(175, 500, title_quit):
            run_game.game_state.change(State.QUIT)
            return

        pygame.display.update()
        clock.tick(60)
