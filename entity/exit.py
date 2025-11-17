import pygame
from environment import Environment

class Exit(pygame.sprite.Sprite):
    def __init__(self, pos: (int,int)):
        super().__init__()
        RECTSIZE = Environment.RECTSIZE
        self.image = pygame.Surface((RECTSIZE, RECTSIZE))
        self.image.fill((200, 200, 0))
        self.rect = self.image.get_rect(topleft=pos)