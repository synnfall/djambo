import pygame
import os
from environment import Environment
from core.direction import Direction

class Bullet(pygame.sprite.Sprite):

    direction: Direction
    wallSprites: pygame.sprite.Group

    def __init__(self, pos: tuple[int, int], direction: Direction, wallSprites: pygame.sprite.Group):
        super().__init__()
        RECTSIZE = Environment.RECTSIZE // 4
        self.RECTSIZE = RECTSIZE
        path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'feu.png')
        path = os.path.abspath(path)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (RECTSIZE, RECTSIZE))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = direction
        self.speed = Environment.PLAYERSPEED * 1.75
        self.wallSprites = wallSprites

    def update(self):
        self.move()
        self.check_collision()

    def move(self):
        match self.direction:
            case Direction.HAUT:
                self.rect.y -= self.speed
            case Direction.BAS:
                self.rect.y += self.speed
            case Direction.GAUCHE:
                self.rect.x -= self.speed
            case Direction.DROITE:
                self.rect.x += self.speed
    
    def check_collision(self):
        if pygame.sprite.spritecollideany(self, self.wallSprites):
            self.kill()
        if self.rect.y > (Environment.HEIGHT-Environment.RECTSIZE) - self.RECTSIZE or \
            self.rect.y < 0 or \
            self.rect.x > Environment.WIDTH-self.RECTSIZE or\
            self.rect.x < 0:
            self.kill()