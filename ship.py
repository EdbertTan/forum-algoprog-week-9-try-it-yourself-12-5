import pygame
 
class playership:
    def __init__(self, gamedisplay):
        self.screen = gamedisplay.screen
        self.settings = gamedisplay.settings
        self.rectscreen = gamedisplay.screen.get_rect()
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.rectscreen.midleft
        self.y = float(self.rect.y)
        self.upmove = False
        self.downmove = False
    def blitship(self):
        self.screen.blit(self.image, self.rect)
    def shipupd(self):
        if self.upmove and self.rect.top > 0:
            self.y -= self.settings.playerspeed
        if self.downmove and self.rect.bottom < self.rectscreen.bottom:
            self.y += self.settings.playerspeed
        self.rect.y = self.y