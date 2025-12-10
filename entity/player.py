import pygame
import os
from environment import Environment
from core.direction import Direction
from entity.bullet import Bullet

class Player(pygame.sprite.Sprite):

    TIME_BETWEEN_SHOT: int = 500
    direction: Direction

    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        RECTSIZE = Environment.RECTSIZE*0.80
        self.RECTSIZE = RECTSIZE
        self.loadskin()
        self.image = self.skinDirection[Direction.DROITE]
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = Environment.PLAYERSPEED
        self.direction = Direction.DROITE
        self.lastShotTime = 0

    def loadskin(self):
        RECTSIZE = self.RECTSIZE
        back = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'player','back.png'))
        front = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'player','front.png'))
        left = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'player','left.png'))
        right = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'player','right.png'))
        self.skinDirection = {
            Direction.DROITE: pygame.transform.scale(pygame.image.load(right).convert_alpha(), (RECTSIZE, RECTSIZE)),
            Direction.GAUCHE: pygame.transform.scale(pygame.image.load(left).convert_alpha(), (RECTSIZE, RECTSIZE)),
            Direction.HAUT:   pygame.transform.scale(pygame.image.load(back).convert_alpha(), (RECTSIZE, RECTSIZE)),
            Direction.BAS:    pygame.transform.scale(pygame.image.load(front).convert_alpha(), (RECTSIZE, RECTSIZE))
        }

    def update(self, wallSprites, bulletSprites):
        self.move(wallSprites)
        self.shoot(wallSprites, bulletSprites)

    def move(self, wallSprites):
        speed = self.speed
        keys = pygame.key.get_pressed()

        oldDir = self.direction
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction = Direction.GAUCHE
            self.rect.x -= speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.x += 1
            if self.rect.x < 0:
                self.rect.x = 0
                    
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = Direction.DROITE
            self.rect.x += speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.x -= 1
            if self.rect.x > Environment.WIDTH-self.RECTSIZE:
                self.rect.x = Environment.WIDTH-self.RECTSIZE

        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.direction = Direction.HAUT
            self.rect.y -= speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.y += 1
            if self.rect.y < 0:
                self.rect.y = 0

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = Direction.BAS
            self.rect.y += speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.y -= 1
            if self.rect.y > (Environment.HEIGHT-Environment.RECTSIZE) - self.RECTSIZE:
                self.rect.y = (Environment.HEIGHT-Environment.RECTSIZE) - self.RECTSIZE
        
        if( oldDir != self.direction):
            self.image = self.skinDirection[self.direction]

    def shoot(self, wallSprites, bulletSprites):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        time = pygame.time.get_ticks()
        if(keys[pygame.K_SPACE] or mouse[0]) and (time - self.lastShotTime > self.TIME_BETWEEN_SHOT):
            self.lastShotTime = time
            bulletSprites.add(Bullet(self.rect.center, self.direction, wallSprites))