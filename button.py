import pygame

display_width = 1600
display_height = 900
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)
lightgreen = (0, 255, 0)
lightred = (255, 0, 0)

class Button:
    def __init__(self,msg,x,y,w,h,inactive,active,action=None):
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = inactive
        self.ac = active
        self.action = action
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
    #function to make a button with adjustable size and position
    def make_button(self):
        if self.x + self.w > self.mouse[0] > self.x and self.y+self.h > self.mouse[1] > self.y:
            pygame.draw.rect(gameDisplay, self.ac,(self.x,self.y,self.w,self.h))
            if self.click[0] == 1 and self.action != None:
                intro = False
                self.action()
        else:
            pygame.draw.rect(gameDisplay, self.ic,(self.x,self.y,self.w,self.h))

        smallText = pygame.font.SysFont("impact.ttf",50)
        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = ( (self.x+(self.w/2)), (self.y+(self.h/2)) )
        gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()