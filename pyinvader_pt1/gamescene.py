import pygame
import random

class Gamescene(object):

    def __init__(self, w, h):
        pygame.init()

        self.width = w
        self.height = h
        self.scene  = pygame.display.set_mode((w,h))
        self.caption = pygame.display.set_caption("PyInvader")
        self.icon    = pygame.image.load("assets/icon.png")

        self.points = 0
        self.gameloop = True

        self.font = 'assets/ARCADECLASSIC.TTF'
        self.lives = 3
        self.lifetext = 'assets/icon.png'
        self.life = pygame.image.load(self.lifetext)

        self.highscores = self.getHighScores()

        pygame.display.set_icon(self.icon)

        self.bgimg = 'assets/b'+str(random.randint(1,6))+'.jpg'

        if(self.bgimg != ''):
            self.bg = pygame.image.load(self.bgimg)

        self.bgc = (51,51,51)

    def setBackground(self):
        self.scene.fill(self.bgc)
        if(self.bg != None):
            self.scene.blit(self.bg, (0,0) )

    def displayLives(self):
        for i in range(self.lives):
            self.scene.blit(self.life, (self.width - (37 + 37*i), (10)))

    def update(self):
        self.setScoreBoard()
        self.displayLives()
        pygame.display.update()

    def setScoreBoard(self):
        font = pygame.font.Font('freesansbold.ttf',32)

        text = font.render('[ '+str(self.points)+' ]', True, (255,255,255) )
        self.scene.blit(text, (10, 10) )

    def setHighScores(self):
        hsFile = open("scores.txt","w")
        self.highscores.append(self.points)
        self.highscores.sort()
        for score in self.highscores:
            hsFile.write("%i\n" % score)
        hsFile.close()

    def getHighScores(self):
        hsFile = open("scores.txt","r")
        scores = hsFile.readlines()
        hsFile.close()
        scores = [int(i) for i in scores]
        return scores

    def setPoints(self, points):
        self.points += points
        self.setScoreBoard()

    def resetGame(self):
        self.gameloop = False
        self.points = 0
        self.lives = 3

    def gameOver(self,result):
        # self.gameloop = False
        font = pygame.font.Font(self.font, 32)

        if(result == "win"):
             text = font.render('YOU WIN!!!  '+str(self.points)+' pts', True, (255,255,255) )
        if(result == "loss"):
             text = font.render('GAME OVER! '+str(self.points)+' pts', True, (255,255,255) )

        self.scene.blit(text, ( self.width // 2 - 160 , self.height //2 ) )
        self.update()
        self.setHighScores()
        self.resetGame()
