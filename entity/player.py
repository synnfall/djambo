import pygame
from environment import Environment

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: (int,int)):
        super().__init__()
        RECTSIZE = Environment.RECTSIZE*0.80
        self.image = pygame.Surface((RECTSIZE, RECTSIZE))
        self.image.fill((0, 200, 50))
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = Environment.PLAYERSPEED

    def update(self, wallSprites):
        self.move(wallSprites)

    def move(self, wallSprites):
        speed = self.speed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.x += 1
                    
        elif keys[pygame.K_RIGHT]:
            self.rect.x += speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.x -= 1

        if keys[pygame.K_UP]:
            self.rect.y -= speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.y += 1
        elif keys[pygame.K_DOWN]:
            self.rect.y += speed
            if pygame.sprite.spritecollideany(self, wallSprites):
                while pygame.sprite.spritecollideany(self, wallSprites):
                    self.rect.y -= 1