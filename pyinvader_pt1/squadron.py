import pygame
import random
from enemy import Enemy

class Squadron(object):

    def __init__(self, units, rows):
        self.ships = []
        self.units = units
        self.rows = rows
        self.rock = False
        #self.meteor =
        self.drop = 0

        columns = units // rows

        for row in range(rows):
            for i in range(columns):
                self.ships.append(Enemy(i*120, row*90))

        self.speed = self.ships[0].speed

    def update(self, s, w):
        enmDown = False

        #if(self.drop == 4):
            #self.rock = True

        for enemy in self.ships:
            if(enemy.x <= 0):
                self.speed = enemy.speed
                enmDown = True
            elif(enemy.x > (w - enemy.w) ):
                self.speed = -enemy.speed
                enmDown = True

            if(enemy.y > 520-enemy.h):
                s.gameOver("loss")

        chgX = self.speed

        if(enmDown):
            chgY = 20
            enmDown = False
            self.drop += 1
        else:
            chgY = 0
        i = 0
        for ship in self.ships:
            ship.move(chgX, chgY)
            s.scene.blit( ship.enemy, (ship.x, ship.y) )
            if(i==12):
                target = pygame.image.load('assets/target.png')
                s.scene.blit( target, ( ship.cX-4, ship.cY-4 ) )
            i += 1

    def hitShip(self, shipNum):
        del(self.ships[shipNum])
            


















        
