import sys

import pygame

from settings import setty
from ship import playership
from bullet import Bulletsprite

class playercharacter:

    def __init__(self):
        pygame.init()
        self.settings = setty()

        self.screen = pygame.display.set_mode(
                (self.settings.swidth, self.settings.sheight))
        pygame.display.set_caption("Sideways Shooter Game")

        self.ship = playership(self)
        self.bullets = pygame.sprite.Group()

    def screenupd(self):
        self.screen.fill(self.settings.backgroundcolor)
        self.ship.blitship()
        for bullet in self.bullets.sprites():
            bullet.makebullet()
        pygame.display.flip()

    def chackactions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.checkkeyinput(event)
            elif event.type == pygame.KEYUP:
                self.checkreleaseinput(event)

    def checkkeyinput(self, event):
        if event.key == pygame.K_UP:
            self.ship.upmove = True
        elif event.key == pygame.K_DOWN:
            self.ship.downmove = True
        elif event.key == pygame.K_SPACE:
            self.shoot()
        elif event.key == pygame.K_q:
            sys.exit()

    def checkreleaseinput(self, event):
        if event.key == pygame.K_UP:
            self.ship.upmove = False
        elif event.key == pygame.K_DOWN:
            self.ship.downmove = False

    def shoot(self):
        if len(self.bullets) < self.settings.bulletsallowed:
            newblt = Bulletsprite(self)
            self.bullets.add(newblt)

    def bulletupd(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)

    def startgameprog(self):
        while True:
            self.chackactions()
            self.ship.shipupd()
            self.bulletupd()
            self.screenupd()

if __name__ == '__main__':
    gamedisplay = playercharacter()
    gamedisplay.startgameprog()