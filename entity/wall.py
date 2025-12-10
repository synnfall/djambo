import pygame
import os
from environment import Environment

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], spritesLst):
        RECTSIZE = Environment.RECTSIZE
        super().__init__(spritesLst)
        path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'wall.png')
        path = os.path.abspath(path)

        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (RECTSIZE, RECTSIZE))

        self.rect = self.image.get_rect(topleft=pos)