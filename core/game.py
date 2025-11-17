import pygame
from environment import Environment
from core.levelLoader import LevelLoader
from entity.player import Player
from entity.exit import Exit
from entity.wall import Wall

class Game:
    screen: pygame.Surface

    walls: list[Wall]
    player: Player
    exitDoor: Exit
    
    levelLoader: LevelLoader

    def __init__(self):
        pygame.init()
        self.levelLoader = LevelLoader()
        self.screen = pygame.display.set_mode((Environment.WIDTH, Environment.HEIGHT))

        self.wallSprites = pygame.sprite.Group()
        level = self.levelLoader.loadLevel(0, self.wallSprites)
        self.walls = level['Wall']
        self.player = level["Player"]
        self.exitDoor = level["Exit"]

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()
        pygame.quit()
    
    def draw(self):
        self.screen.fill((30, 30, 30))
        self.wallSprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.exitDoor.image, self.exitDoor.rect)
        pygame.display.flip()