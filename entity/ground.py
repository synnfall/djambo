import pygame
from environment import Environment

class Ground(pygame.sprite.Sprite):
    def __init__(self, pos: (int,int), spritesLst):
        RECTSIZE = Environment.RECTSIZE
        super().__init__(spritesLst)
        self.image = pygame.Surface((RECTSIZE, RECTSIZE))
        self.image.fill((200, 200, 200))  # gris
        self.rect = self.image.get_rect(topleft=pos)