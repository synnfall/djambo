import pygame
from environment import Environment
from core.levelLoader import LevelLoader
from entity.player import Player
from entity.exit import Exit
from entity.wall import Wall
from entity.ground import Ground

class Game:
    screen: pygame.Surface

    walls: list[Wall]
    grounds: list[Ground]
    player: Player
    exitDoor: Exit
    
    levelLoader: LevelLoader

    clock: pygame.time.Clock

    def __init__(self):
        pygame.init()
        self.levelLoader = LevelLoader()
        self.screen = pygame.display.set_mode((Environment.WIDTH, Environment.HEIGHT))

        self.wallSprites = pygame.sprite.Group()
        self.groundSprites = pygame.sprite.Group()

        level = self.levelLoader.loadLevel(0, self.wallSprites, self.groundSprites)
        self.walls = level['Wall']
        self.player = level["Player"]
        self.exitDoor = level["Exit"]
        self.grounds = level["Ground"]

        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.player.update(self.wallSprites)
            self.draw()
        pygame.quit()
    
    def draw(self):
        self.screen.fill((50, 50, 50))
        #self.wallSprites.draw(self.screen)
        #self.groundSprites.draw(self.screen)
        self.screen.blit(self.exitDoor.image, self.exitDoor.rect)
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.flip()