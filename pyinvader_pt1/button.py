import pygame

class Button(object):

    def __init__(self, thid, scene, introObj, color, x, y, w, h, image, text=''):
        self.color  = color
        self.x      = x
        self.y      = y
        self.width  = w
        self.height = h
        self.scene  = scene
        self.image  = image # This is a bool

        self.thid = thid
        self.intro = introObj

        self.fontfile = "assets/ARCADECLASSIC.TTF"
        self.font = pygame.font.Font(self.fontfile, 30)

        if(image):
            self.text = text+".png"
            self.imgh = text+"_.png"

            self.norm = pygame.image.load(self.text)
            self.hovr = pygame.image.load(self.imgh)
        else:
            self.text = text

    def draw(self, outline=False):
        # Call this method to draw the button on the screen

        # if(outline):
        #   pygame.draw.rect(self.scene, outline, (self.x-2, self.y-2, self.width+4, self.height+4), i)


        #pygame.draw.rect(self.scene, (0,0,0), (self.x, self.y, self.width, self.height), 1)

        if(not self.image):
            text = self.font.render(self.text, 1, (0,0,0))
            self.scene.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        else:
            self.scene.blit(self.norm, (self.x + ((self.width - self.hovr.get_width())/2), self.y + ((self.height - self.hovr.get_height()) / 2)))

    def isOver(self, pos):
        # pos is the position or a tuple of x,y coordinates
        if (pos[0] > self.x and pos[0] < self.x + self.width):
            if (pos[1] > self.y and pos[1] < self.y + self.height):
                return True
        return False

    def update(self):
        pos = pygame.mouse.get_pos()
        event = pygame.event.wait()

        if (self.isOver(pos)):
            # pygame.draw.rect(self.scene, (255,255,255), (self.x, self.y, self.width, self.height), 1)
            if(self.image):
                self.scene.blit(self.hovr, ( self.x + ( (self.width - self.hovr.get_width())/2), self.y + ( ( self.height - self.hovr.get_height()) /2) ))
                # self.scene.blit(self.hovr ( self.x + ( (self.width - self.hovr.get_width())/2), self.y + ( ( self.height - self.hovr.get_height()) /2) ))
                if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP):
                    self.intro.setChoice(self.thid)
                    print('clicked : ' + str(self.thid))
        else:
            self.draw()
