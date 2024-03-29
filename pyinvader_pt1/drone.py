import pygame
import random

class Drone(object):

    IMAGE = ['assets/drone1.png','assets/drone2.png','assets/drone3.png','assets/drone4.png']

    def __init__(self, x, y):
        self.hp = random.randint(1,4)
        self.enemy = pygame.image.load(self.IMAGE[self.hp-1])
        self.x = x
        self.y = y
        self.w = 93
        self.h = 84
        self.cX = x + (self.w // 2)
        self.cY = y + (self.y // 2)
        self.speed = 1.25
        self.down = False
        self.points = self.hp*100

        self.boom = pygame.mixer.Sound('assets/boom.wav')
        self.hit  = pygame.mixer.Sound('assets/hit.wav')

        self.target = 'assets/target.png'

    def move(self, x, y):
        self.x += x
        self.y += y
        self.cX = self.x + (self.w // 2)
        self.cY = self.y + (self.h // 2)

    def gotHit(self):
        self.enemy = pygame.image.load(self.IMAGE[self.hp-1])
