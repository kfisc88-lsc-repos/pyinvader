import pygame
import random
from drone import Drone

class Diver(Drone):
    """docstring for Fighter."""

    IMAGE = ['assets/diver1.png','assets/diver2.png','assets/diver3.png','assets/diver4.png']

    def __init__(self, x, y):
        super().__init__(x, y)
        self.hp = random.randint(1,4)
        self.enemy = pygame.image.load(self.IMAGE[self.hp-1])
