import pygame
import random
from drone import Drone

class Fighter(Drone):
    """docstring for Fighter."""

    IMAGE = ['assets/fighter1.png','assets/fighter2.png','assets/fighter3.png','assets/fighter4.png']
    BULLET = 'assets/enmLaser.png'

    def __init__(self, x, y):
        super().__init__(x, y)
        self.hp = random.randint(1,4)
        self.enemy = pygame.image.load(self.IMAGE[self.hp-1])
