import pygame
from pygame.sprite import Sprite
 
class Bulletsprite(Sprite):
    def __init__(self, gamedisplay):
        super().__init__()
        self.screen = gamedisplay.screen
        self.settings = gamedisplay.settings
        self.color = self.settings.bulletcolor
        self.rect = pygame.Rect(0, 0, self.settings.bulletwidth,self.settings.bulletheight)
        self.rect.midright = gamedisplay.ship.rect.midright
        self.x = float(self.rect.x)
    def makebullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    def update(self):
        self.x += self.settings.bulletspeed
        self.rect.x = self.x