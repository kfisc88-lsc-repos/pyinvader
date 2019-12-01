import pygame
from button import Button

class Intro(object):
    """docstring for Intro."""

    def __init__(self, w, h):
        pygame.init()
        self.width = w
        self.height = h

        self.scene = pygame.display.set_mode((w,h))
        self.caption = pygame.display.set_caption('PyInvaders')
        self.icon = pygame.image.load('assets/icon.png')

        self.introloop = True
        self.font = 'assets/ARCADECLASSIC.TTF'
        pygame.display.set_icon(self.icon)

        self.game = False
        self.bgc = (128,51,51)
        self.bgimg = 'assets/intro.jpg'
        self.bg = pygame.image.load(self.bgimg)

        self.choice = "x"

        self.buttons = self.setButton()

    def setTitle(self):
        font = pygame.font.Font(self.font, 90)
        text = font.render('PyInvader', True, (255, 255, 255))
        self.scene.blit(text, (self.width // 2 - 220, 200))

    def setChoiceText(self):
        font = pygame.font.Font(self.font, 20)
        text = font.render('Pick a ship', True, (255, 255, 255))
        self.scene.blit(text, (self.width // 2 - (text.get_width()/2), 460))

    def setButton(self):
        buttons = []
        buttons.append(Button(1, self.scene, self, (254,254,254,0), 140, 510, 120, 81, True, 'assets/player'))
        buttons.append(Button(2, self.scene, self, (254,254,254,0), 340, 510, 120, 81, True, 'assets/player2'))
        buttons.append(Button(3, self.scene, self, (254,254,254,0), 540, 510, 120, 81, True, 'assets/player3'))
        print(buttons)

        return buttons

    def showButtons(self):
        for b in self.buttons:
            b.update()

    def setBackground(self):
        self.scene.fill(self.bgc)
        self.scene.blit(self.bg, (0,0))

    def update(self):
        self.setBackground()
        self.setTitle()
        self.setChoiceText()
        self.showButtons()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()

        pygame.display.update()

    def startGame(self):
        return self.game

    def getChoice(self):
        return self.choice

    def setChoice(self, choice):
        self.choice = choice
        self.game = True

    def events(self):
        if (self.choice != 'x'):
            self.introloop = False
        return [self.introloop, self.choice]
