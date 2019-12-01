import pygame
import random
from drone import Drone
from fighter import Fighter
from diver import Diver
# from meteor import Meteor

class Squadron(object):

    def __init__(self, gamescene, units, rows, pattern = []):
        self.ships = []
        self.units = units
        self.rows = rows
        self.rock = False
        #self.meteor = Meteor(700, 0)
        self.drop = 0
        self.player = gamescene

        self.ships = self.setSquadron(units, rows, pattern)

        # columns = units // rows
        #
        # for row in range(rows):
        #     for i in range(columns):
        #         self.ships.append(Enemy(i*120, row*90))

        self.speed = self.ships[0].speed

    def setEnemy(self, enum, x, y):
        if (enum == 0):
            return Drone(x,y)
        elif(enum == 1):
            return Fighter(x,y)
        elif(enum == 2):
            return Diver(x,y)

    def setSquadron(self, u, r, p):
        ships = []
        columns = u // r
        if (len(p) == 0):
            for row in range(r):
                for i in range(columns):
                    ships.append(Drone(i*120, row*90))
        else:
            ix = 0
            for row in range(r):
                for i in range(columns):
                    ships.append(self.setEnemy(p[ix], i*120, row*90))
                    ix += 1

        return ships

    def squadRetreat(self):
        for enemy in self.ships:
            enemy.y -= 200
        self.player.lives -= 1
        if (self.player.lives < 0):
            self.player.gameOver("loss")

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
                self.squadRetreat()
                # s.gameOver("loss")

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

            # adds a dot to 12th ship in squadron for debugging
            if(i==12):
                target = pygame.image.load('assets/target.png')
                s.scene.blit( target, ( ship.cX-4, ship.cY-4 ) )
            i += 1

    def hitShip(self, shipNum):
        del(self.ships[shipNum])
