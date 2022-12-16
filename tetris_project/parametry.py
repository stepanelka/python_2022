import pygame
import Font as f

pygame.init()

#размер экрана
size = (700, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#текст счета, паузы, начала, выхода, рестарта и продолжения(выхода из паузы)
title_score = f.font.render('СЧЕТ:', True, pygame.Color('purple'))
title_pause = f.button_font.render('ПАУЗА', True, pygame.Color('purple'))
title_start = f.main_font.render('НАЧАТЬ', True, pygame.Color('purple'))
title_quit = f.main_font.render('ВЫЙТИ', True, pygame.Color('purple'))
title_restart = f.main_font.render('ЗАНОВО', True, pygame.Color('purple'))
title_resume = f.main_font.render('ПРОДОЛЖИТЬ', True, pygame.Color('purple'))

#названия фона
title_theme1 = f.button_font.render('ИНЕЙ', True, pygame.Color('purple'))
title_theme2 = f.button_font.render('БАБОЧКА', True, pygame.Color('purple'))
title_theme3 = f.button_font.render('РУКИ', True, pygame.Color('purple'))
title_theme4 = f.button_font.render('ВОДА', True, pygame.Color('purple'))
title_theme5 = f.button_font.render('КОРОЛЬ', True, pygame.Color('purple'))
title_theme6 = f.button_font.render('ГИТАРИСТ', True, pygame.Color('purple'))
title_theme7 = f.button_font.render('ТЫК!', True, pygame.Color('purple'))

#названия уровней сложности
title_level1 = f.button_font.render('УРОВЕНЬ 1', True, pygame.Color('purple'))
title_level2 = f.button_font.render('УРОВЕНЬ 2', True, pygame.Color('purple'))
title_level3 = f.button_font.render('УРОВЕНЬ 3', True, pygame.Color('purple'))
title_level4 = f.button_font.render('УРОВЕНЬ 4', True, pygame.Color('purple'))
title_level5 = f.button_font.render('УРОВЕНЬ 5', True, pygame.Color('purple'))

#названия музыки
title_music1 = f.button_font.render('ДVДTДR_1', True, pygame.Color('purple'))
title_music2 = f.button_font.render('APOCALYPTICA', True, pygame.Color('purple'))
title_music3 = f.button_font.render('ДVДTДR_2', True, pygame.Color('purple'))
title_music4 = f.button_font.render('DRAKE', True, pygame.Color('purple'))
title_music5 = f.button_font.render('LADY GAGA', True, pygame.Color('purple'))
title_music6 = f.button_font.render('KANYE WEST', True, pygame.Color('purple'))
title_music7 = f.button_font.render('ТЫК!', True, pygame.Color('purple'))


#цвета
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
PURPLE1 = (121, 44, 240)
PURPLE2 = (101, 0, 178)
PURPLE3 = (189, 134, 254)
PURPLE4 = (228, 13, 251)
PURPLE5 = (55, 13, 251)
PURPLE6 = (202, 117, 176)
colors = [BLACK, PURPLE1, PURPLE2, PURPLE3, PURPLE4, PURPLE5, PURPLE6]