import pygame

pygame.init()

button_sound = pygame.mixer.Sound('sounds/button.wav')
#задает все используемые мелодии
def set_sound(num):
    global game_sound
    game_sound = pygame.mixer.music.load('sounds/melody{}.mp3'.format(num))
