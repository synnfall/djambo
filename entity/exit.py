import pygame
import os
from environment import Environment
from entity.player import Player

class Exit(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        RECTSIZE = Environment.RECTSIZE

        path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'door.png')
        path = os.path.abspath(path)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (RECTSIZE, RECTSIZE))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, player: Player):
        GrpPlayer = pygame.sprite.GroupSingle()
        GrpPlayer.add(player)
        if pygame.sprite.spritecollideany(self, GrpPlayer):
            pass