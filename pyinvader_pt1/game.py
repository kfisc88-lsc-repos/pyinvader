import pygame

from gamescene import Gamescene
from player import Player
from squadron import Squadron
from level import Level
from intro import Intro


def main():
    h = 600
    w = 800
    g = Gamescene(w,h)
    i = Intro(w,h)
    pygame.mixer.music.load('assets/levelMusic.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    play = True
    intro = True
    game = False

    while play:
        pnum = 0
        if (intro):
            i.update()
            checkEvents = i.events()
            intro = checkEvents[0]
            pnum = checkEvents[1]
            game = i.startGame()
        if (game):
            g.gameloop = True
            gameloop(h, w, g, pnum)
            game = g.gameloop
        else:
            intro = True
            i.choice = "x"
            i.game = False
            i.update() # <--------------------May need fixing

    pygame.mixer.music.stop()

def gameloop(h, w, g, pnum):
    p = Player(390, 520, 2, w, pnum)
    # s = Squadron(15,3)
    start = 1
    maxLevel = 3

    l = Level(start, g, False, maxLevel)
    s = l.squad

    play = True
    while(play):

        g.setBackground()

        p.controls(pygame.event.get())



        p.update(g,s)
        # s.update(g,w)
        l.update()
        g.update()
        # if(len(s.ships) == 0):
        #     g.gameOver("win")
        if (s != False):
            if (len(s.ships) == 0):
                l.advanceLevel()
                s = l.squad
                play = g.gameloop
            else:
                play = g.gameloop
        else:
            play = s
        play = g.gameloop



main()
