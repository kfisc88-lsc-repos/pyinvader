import pygame

from gamescene import Gamescene
from player import Player
from squadron import Squadron

def main():
    h = 600
    w = 800
    g = Gamescene(w,h)
    pygame.mixer.music.load('assets/levelMusic.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)


    gameloop(h,w,g)

    pygame.mixer.music.stop()

def gameloop(h,w,g):
    p = Player(390,520,2,w)
    s = Squadron(15,3)
    
    play = True
    while(play):

        g.setBackground()

        p.controls(pygame.event.get())



        p.update(g,s)
        s.update(g,w)
        g.update()
        if(len(s.ships) == 0):
            g.gameOver("win")

        play = g.gameloop
        


main()
