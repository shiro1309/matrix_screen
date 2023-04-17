import os
import pygame as pg
from random import choice, randrange

res = width, height = 1600, 900
FONT_SIZE = 40
alpha_value = 0

pg.init()
screen = pg.display.set_mode(res)
clock = pg.time.Clock()
font = pg.font.Font('font/ms mincho.ttf', FONT_SIZE, bold=True)
katakana = [chr(int('0x30a0',16) + i) for i in range(96)]

while True:
    screen.fill((100,100,100))
    surf = font.render(katakana[3], True, pg.Color('lightgreen'))
    screen.blit(surf, (400,400))
    
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    
    pg.display.flip()