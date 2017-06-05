#encoding:utf-8
#from settings import Settings
import pygame
from pygame.sprite import Sprite
class Picture(Sprite):
    def __init__(self, screen, label, x, y):
        # 图片的属性
        super(Picture, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/"+label+".jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y


    def blitme(self):
        self.screen.blit(self.image,self.rect)