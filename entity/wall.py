import pygame
from environment import Environment

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos: (int,int), spritesLst):
        RECTSIZE = Environment.RECTSIZE
        super().__init__(spritesLst)
        self.image = pygame.Surface((RECTSIZE, RECTSIZE))
        self.image.fill((100, 100, 100))  # gris
        self.rect = self.image.get_rect(topleft=pos)