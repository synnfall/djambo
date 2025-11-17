import pygame
from environment import Environment

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: (int,int)):
        super().__init__()
        RECTSIZE = Environment.RECTSIZE
        self.image = pygame.Surface((RECTSIZE, RECTSIZE))
        self.image.fill((0, 200, 50))
        self.rect = self.image.get_rect(topleft=pos)

    def update():
        pass