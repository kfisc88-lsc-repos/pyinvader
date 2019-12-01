import pygame
import random
from squadron import Squadron

class Level(object):
    """docstring for Level."""

    def __init__(self, lvlnum, gamescene, infinite=False, maxlvl=3):

        self.level = lvlnum
        self.g = gamescene
        self.w = self.g.width
        self.infinite = infinite
        self.maxlvl = maxlvl
        self.squad = self.setSquad(lvlnum, 15, 3)

    def advanceLevel(self):
        self.level += 1
        if (self.level > self.maxlvl and not self.infinite):
            self.g.gameOver("win")
            return False
        else:
            # Setting Squad
            self.squad = self.setSquad(self.level, 15, 3)
            return True

    def setSquad(self, lvl, units, rows):
        print('setSquad lvl: ' + str(lvl))
        level = []

        level.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        level.append([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        level.append([1,0,2,0,1,0,2,0,1,0,2,0,1,0,2])

        if (self.infinite or lvl-1 < self.maxlvl):
            #print(lvl)
            # now load Level

            if (lvl-1 > len(level)):
                # out of normal levels
                # call a random levels
                # append to level list
                # set pattern to level-1
                print('reached last level - I need a random one')

            # print(level(lvl-1))
            pattern = level[lvl-1]
            return Squadron(self.g, units, rows, pattern)
        else:
            # print('gameover?')
            self.g.gameOver("win")
            return False

    def update(self):
        if (self.squad != False):
            self.squad.update(self.g, self.w)
