#encoding:utf-8

import pygame
from settings import Settings
from pygame.sprite import Group
from picture import Picture
import functions as f
import csv


def load_image():

    pygame.init()
    ai_settings = Settings()  # 将所有的参数变化与settings.py相联系
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Result")

    # 创建一个图片集的集合
    pictures = Group()
    filename = "coordinate.csv"
    with open(filename) as f1:
        reader = csv.reader(f1)
        labels, xs, ys = [], [], []
        for row in reader:
            labels.append(row[0])
            xs.append(float(row[1]))
            ys.append(float(row[2]))
    #while True:
     #   for a in range(0,3):
    a=0
    for a in range(736):
            label = labels[a]
            x = 200*xs[a]
            y = 200*ys[a]
            Picture(screen, label, x, y)
            f.add_pic(screen, label, x, y, pictures)
    while True:
            f.check_events()
            f.update_screen(ai_settings, screen, pictures)





load_image()