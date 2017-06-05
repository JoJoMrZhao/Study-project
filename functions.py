#encoding:utf-8
import sys
import pygame
from picture import Picture

def check_events():
    #检查各类事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings, screen, pictures):
    #绘制
    screen.fill(ai_settings.bg_color)
    pictures.draw(screen)
    pygame.display.flip()
def add_pic(screen, label, x, y, pictures):
    picture = Picture(screen, label, x, y)
    pictures.add(picture)