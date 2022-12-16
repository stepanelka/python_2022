import pygame

pygame.init()

#варианты фона начального меню, фона при выборе фона для игры, уровня и музыки
bckg = pygame.image.load('img/bg1.jpg')
bg_end = pygame.image.load('img/bg_end.jpg')
bg_menu = pygame.image.load('img/bg_menu.jpg')
themeimage = pygame.image.load('img/choose_theme.jpg')
levelimage = pygame.image.load('img/choose_level.jpg')
soundimage = pygame.image.load('img/choose_music.jpg')

#установка фона для основной части игры
def set_theme(num):
    global bckg
    bckg = pygame.image.load(r'img/bg{}.jpg'.format(num))