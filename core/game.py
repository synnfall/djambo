import pygame
from environment import Environment

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Environment.WIDTH, Environment.HEIGHT))

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()
        pygame.quit()
    
    def draw(self):
        pygame.display.flip()