import pygame
import random
import math

class Player(object):

    def __init__(self, x, y, speed, screen):
        self.shipImage = 'assets/player.png'
        self.ship = pygame.image.load(self.shipImage)
        self.w = 112
        self.h = 75
        self.x = x
        self.y = y

        self.laser = {'x':0,'y':520, 'chgY':10, 'beam':pygame.image.load('assets/plyLaser.png') }

        self.move = 0
        self.speed = speed
        self.screen = screen

        self.state = "ready"
        self.pewpew = "assets/NFF-laser-gun.wav"
        self.sound  = pygame.mixer.Sound(self.pewpew)


    def controls(self, events):

        for event in events:

            #Quit
            if(event.type == pygame.QUIT):
                running = False
                pygame.quit()
                quit()

            
            # check for left and right and spacebar
            if(event.type == pygame.KEYDOWN):
                #print('a key has been pressed')

                if(event.key == pygame.K_LEFT):
                    self.move = -self.speed
                    
                elif(event.key == pygame.K_RIGHT):
                    self.move = self.speed

                elif(event.key == pygame.K_SPACE):
                    #print('space bar pressed')
                    if(self.state == "ready"):
                        self.fire( self.x - 4 + (self.w // 2), self.laser['y'])

            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    self.move = 0.0


    def update(self,s,squad):

        self.x += self.move

        if(self.x <= 0):
            self.x = 0
        elif(self.x >= (self.screen - self.w)):
             self.x = self.screen - self.w

        s.scene.blit(self.ship, (self.x, self.y) )

        #now for the laser

        if(self.state == "fired"):
            self.fire(self.laser['x'], self.laser['y'])
            self.laser['y'] -= self.laser['chgY']
            s.scene.blit(self.laser['beam'], (self.laser['x'], self.laser['y']) )
        
            #check for collision
            i = 0
            for ship in squad.ships:

                xes = math.pow(ship.cX - self.laser['x'],2)
                yes = math.pow(ship.cY - self.laser['y'],2)

                d = math.sqrt(xes+yes)

                if(d < 45):
                    ship.hp -= 1
                    ship.gotHit()

                    if(ship.hp <= 0):
                        pygame.mixer.Sound.play(ship.boom)
                        squad.hitShip(i)
                        s.setPoints(ship.points)

                    else:
                        pygame.mixer.Sound.play(ship.hit)
                    self.resetLaser()
                i += 1

        if(self.laser['y'] < -10):
            self.resetLaser()



    def resetLaser(self):
        self.state = "ready"
        self.laser['y'] = 520    

    def fire(self, x, y):
        if(self.state == "ready"):
            self.laser['x'] = x
            pygame.mixer.Sound.play(self.sound)
        self.laser['y'] = y
        self.state = "fired"







                
