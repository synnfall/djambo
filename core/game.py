import pygame
from environment import Environment
from core.levelLoader import LevelLoader
from entity.player import Player
from entity.exit import Exit
from entity.wall import Wall
from entity.ground import Ground
from entity.bullet import Bullet

class Game:
    PLAYER_ILLUMINATION_RADIUS = 90
    BULLET_ILLUMINATION_RADIUS = 65
    screen: pygame.Surface

    wallSprites: pygame.sprite.Group

    groundSprites: pygame.sprite.Group

    bulletSprites: pygame.sprite.Group

    player: Player
    exitDoor: Exit
    
    levelLoader: LevelLoader

    clock: pygame.time.Clock
    

    def __init__(self):
        pygame.init()
        self.levelLoader = LevelLoader()
        self.screen = pygame.display.set_mode((Environment.WIDTH, Environment.HEIGHT))

        self.clock = pygame.time.Clock()

        self.night = pygame.Surface((Environment.WIDTH, Environment.HEIGHT))

        self.fontBig = pygame.font.SysFont("Arial", 72, bold=True)
        self.fontBold = pygame.font.SysFont("Arial", 60, bold=True)
        self.fontNormal = pygame.font.SysFont("Arial", 50)
        self.fontSmall = pygame.font.SysFont("Arial", 30)

        self.state = "MENU"
        self.buttonHover = False
        self.buttonRect = None
        self.fontButton = self.fontNormal
        self.btnRestart = None
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            match self.state:
                case "MENU":
                    self.updateMenu()
                    self.drawMenu()
                case "IN_GAME":
                    self.player.update(self.wallSprites, self.bulletSprites)
                    self.exitDoor.update(self.player)
                    self.bulletSprites.update()
                    self.update()
                    self.draw()
                case "WIN":
                    self.win()
                case "LOOSE":
                    self.loose()
        pygame.quit()
    

    def win(self):
        self.screen.fill((20, 50, 20))
        self.drawTextCentered("VICTOIRE !", self.fontBig, -120, (100, 255, 100))
        self.drawTextCentered("Bravo, tu as réussi à sauver un sorcier !", self.fontNormal, -40, (255, 255, 255))
        self.drawTextCentered("Tu veux recommencer pour en sauver d'autres ?", self.fontNormal, 20, (255, 255, 255))
        
        self.drawTextCentered("Appuyez sur ECHAP pour quitter ou R pour recommencer", self.fontSmall, 80, (150, 150, 150))
        mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.btnRestart==None : self.buttonColorRestart = (200, 200, 200)
        self.btnRestart = self.drawTextCentered("REJOUER", self.fontBold, 150, self.buttonColorRestart)

        if self.btnRestart.collidepoint(mousePos):
            self.buttonColorRestart = (255, 50, 50)
            
            if click[0] == 1:
                self.state = "IN_GAME"
                self.loadLevel()
        else:
            self.buttonColorRestart = (200, 200, 200)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.state = "IN_GAME"
            self.loadLevel()

        pygame.display.flip()

    def loose(self):
        self.screen.fill((50, 10, 10))
        self.drawTextCentered("GAME OVER", self.fontBig, -120, (255, 50, 50))
        self.drawTextCentered("Aie, un sorcier est mort à cause de toi...", self.fontNormal, -40, (255, 200, 200))
        self.drawTextCentered("Mais il y en a d'autres, essaie de ne pas les tuer !", self.fontNormal, 20, (255, 200, 200))
        
        self.drawTextCentered("Appuyez sur ECHAP pour quitter ou R pour recommencer", self.fontSmall, 80, (150, 150, 150))

        mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.btnRestart==None : self.buttonColorRestart = (200, 200, 200)
        self.btnRestart = self.drawTextCentered("RÉESSAYER", self.fontBold, 150, self.buttonColorRestart)

        if self.btnRestart.collidepoint(mousePos):
            self.buttonColorRestart = (255, 50, 50)
            
            if click[0] == 1:
                self.state = "IN_GAME"
                self.loadLevel()
        else:
            self.buttonColorRestart = (200, 200, 200)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.state = "IN_GAME"
            self.loadLevel()

        pygame.display.flip()

    def draw(self):
        self.screen.fill((50, 50, 50))
        self.wallSprites.draw(self.screen)
        self.groundSprites.draw(self.screen)
        self.screen.blit(self.exitDoor.image, self.exitDoor.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.bulletSprites.draw(self.screen)
        if not Environment.ADMIN_MODE:
            self.displayNight()
        if(self.time > 5):
            self.drawTextCentered("TEMPS: "+str(round(self.time,1)), self.fontNormal, Environment.HEIGHT/2-28,  (0,255,0))
        else:
            self.drawTextCentered("TEMPS: "+str(round(self.time,1)), self.fontNormal, Environment.HEIGHT/2-28,  (255,0,0)) 
        pygame.display.flip()

    def drawMenu(self):
        self.screen.fill((20, 20, 20))
        self.drawTextCentered("DJAMBO", self.fontBig, -100, (255, 255, 255))
        self.buttonRect = self.drawTextCentered("JOUER", self.fontNormal, 0,  self.colorButton)
        self.drawTextCentered("Appuyez sur ESPACE pour commencer", self.fontSmall, 80, (200, 200, 200))
        pygame.display.flip()
    
    def updateMenu(self):
        self.colorButton = (255, 0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.state = "IN_GAME"
            self.loadLevel()
        if self.buttonRect and self.buttonRect.collidepoint(pygame.mouse.get_pos()):
            self.fontButton = self.fontBold
            self.colorButton = (0, 255, 0)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            self.fontButton = self.fontNormal
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self):
        self.time -= self.clock.get_time() / 1000
        if self.time <=0:
            self.state = "LOOSE"
        if self.exitDoor.rect.colliderect(self.player.rect):
            self.counterWin += 1
            if self.counterWin > 40:
                self.levelNumber += 1
                if Environment.LEVELNUMBER <= self.levelNumber:
                    self.state = "WIN"
                else:
                    self.loadLevel(self.levelNumber)
                     
        else:
            self.counterWin = 0

    def displayNight(self):
        self.night.fill((0, 0, 0))
        playerPos = (self.player.rect.centerx - self.PLAYER_ILLUMINATION_RADIUS, self.player.rect.centery - self.PLAYER_ILLUMINATION_RADIUS)
        self.night.blit(self.player_light_img, playerPos, special_flags=pygame.BLEND_ADD)
        for bullet in self.bulletSprites:
            bulletPos = (bullet.rect.centerx - self.BULLET_ILLUMINATION_RADIUS, bullet.rect.centery - self.BULLET_ILLUMINATION_RADIUS)
            self.night.blit(self.bullet_light_img, bulletPos, special_flags=pygame.BLEND_ADD)
        self.screen.blit(self.night, (0, 0), special_flags=pygame.BLEND_MULT)
    
    def createLightMask(self,radius):
        surface = pygame.Surface((radius * 2, radius * 2))
        surface.fill((0, 0, 0))
        center = (radius, radius)
        for r in range(radius, 0, -1):
            alpha = int(255 * (1 - (r / radius))) 
            pygame.draw.circle(surface, (alpha, alpha, alpha), center, r)
        return surface
    
    def loadLevel(self, levelNumber=0):
        self.levelNumber=levelNumber
        self.wallSprites = pygame.sprite.Group()
        self.groundSprites = pygame.sprite.Group()
        self.bulletSprites = pygame.sprite.Group()
        level = self.levelLoader.loadLevel(levelNumber, self.wallSprites, self.groundSprites)
        self.time = level["Time"]
        self.player = level["Player"]
        self.exitDoor = level["Exit"]
        self.player_light_img = self.createLightMask(self.PLAYER_ILLUMINATION_RADIUS)
        self.bullet_light_img = self.createLightMask(self.BULLET_ILLUMINATION_RADIUS)

    def drawTextCentered(self, text, font, offset, color):
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(Environment.WIDTH // 2, Environment.HEIGHT // 2 + offset))
        self.screen.blit(surface, rect)
        return rect