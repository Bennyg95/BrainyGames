import pygame
from pygame import *
import random
import sys


pygame.init()
mixer.init()
clock = pygame.time.Clock()

length = 640
height = 480

FPS = 200
'''
radius = 15
screen = pygame.display.set_mode((length, height))

startingx = random.randint(radius, length - radius)
startingy = random.randint(radius, height - radius)

change_in_x = random.randint(0, 15)
change_in_y = random.randint(0, 10)
'''
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)

colors = {0 : red, 1 : green, 2 : blue, 3 : darkBlue, 4 : black, 5 : white, 6 : pink}

class BouncingBall:
    def __init__(self, radius, length, height):
        self.radius = radius
        self.length = length
        self.height = height
        
        self.startingx = random.randint(self.radius, self.length - self.radius)
        self.startingy = random.randint(self.radius, self.height - self.radius)
        
        self.change_in_x = random.randint(1, 15)
        self.change_in_y = random.randint(1, 10)
        
        self.center = (self.startingx, self.startingy)
        #self.FPS = random.randint(200, 2000)
        self.FPS = 500
        self.GoingDown = True
        self.GoingRight = True
        
        self.HitRightCorner = False
        self.HitLeftCorner = False
        self.HitTopCorner = False
        self.HitButtomCorner = False
        

    def MakeBall(self, screen, colors):
        pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
        pygame.display.update()
        
 
    def playSound():
        mixer.music.load('blip.ogg')
        mixer.music.play()


    def MovingBall(self, screen, colors):
       
        self.temp_x = self.center[0]
        self.temp_y = self.center[1]
        x = self.center[0]
        y = self.center[1]
        
        if(y >= self.height - self.radius):
            self.HitTopCorner = False
            self.HitButtomCorner = True
            self.HitRightCorner = False
            self.HitLeftCorner = False

            
        if(y <= self.radius):
            self.HitButtomCorner = False
            self.HitTopCorner = True
            self.HitLeftCorner = False
            self.HitRightCorner = False

            
        if(x >= self.length - self.radius):
            self.HitLeftCorner = False
            self.HitRightCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False
            
        if(x <= self.radius):
            self.HitRightCorner = False
            self.HitLeftCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False

        
        self.CheckDirection(screen, colors)
        self.Direction()



    def Direction(self):
        
        x = self.center[0]
        y = self.center[1]
        if(self.temp_x < x and self.temp_y > y):
            self.GoingRight = True
            self.GoingDown = True
        elif(self.temp_x > x and self.temp_y > y):
            self.GoingRight = False
            self.GoingDown = True
        elif(self.temp_x < x and self.temp_y < y):
            self.GoingRight = True
            self.GoingDown = False
        else:
            self.GoingRight = False
            self.GoingDown = False
        

    def CheckDirection(self, screen, colors):
        if(self.HitButtomCorner == True):
            self.hitButtomSide(screen, colors)
            
        elif(self.HitRightCorner == True):
            self.hitRightSide(screen, colors)

        elif(self.HitLeftCorner == True):
            self.hitLeftSide(screen, colors)

        elif(self.HitTopCorner == True):
            self.hitTopSide(screen, colors)

        else:
            self.jumpingAround(screen, colors)
   

        
    def jumpingAround(self, screen, colors):
        x = self.center[0]
        y = self.center[1]
        
        if((y <= self.height - self.radius) and (x <= self.length - self.radius)):
            
            
            x += self.change_in_x
            y += self.change_in_y
            self.center = (x, y)
            
            pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
           
       


    def hitButtomSide(self, screen, colors):
        x = self.center[0]
        y = self.center[1]
        '''
        if( x > self.length - self.radius):
            x = self.length - self.radius
        if(y > self.length - self.radius):
            y = self.length - self.radius
        '''
        if(self.GoingRight == True):
            if((y > self.radius) and (x <= self.length - self.radius)): ##
                
                y -= self.change_in_y
                x += self.change_in_x
                self.center = (x, y)
                
                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
                
        else:
            if((y >= self.radius) and ( x <= self.length - self.radius)):
                
                y -= self.change_in_y
                x -= self.change_in_x
                self.center = (x, y)
                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)




    def hitRightSide(self, screen, colors):
        x = self.center[0]
        y = self.center[1]
        '''
        if( x > self.length - self.radius):
            x = self.length - self.radius
        if(y > self.length - self.radius):
            y = self.length - self.radius ###
        '''
        if(self.GoingDown == True):
            if((x >= self.radius) and ((y <= self.height - self.radius) and ( y >= self.radius))):

                x -= self.change_in_x
                y -= self.change_in_y
                self.center = (x, y)
                
                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
               
        else:
            if((x >= self.radius) and ((y <= self.height - self.radius) and ( y >= self.radius))):

                x -= self.change_in_x
                y += self.change_in_y
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)



    def hitLeftSide(self, screen, colors):
        x = self.center[0]
        y = self.center[1]

        if(self.GoingDown == False):
            if(x <= self.length - self.radius and (y >= self.radius and y <= self.height - self.radius)):
               
                x += self.change_in_x
                y += self.change_in_y
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)

        else:
            if((x <= self.length - self.radius) and ((y >= self.radius) and (y <= self.height - self.radius))):

                x += self.change_in_x
                y -= self.change_in_y
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)


    def hitTopSide(self, screen, colors):
        x = self.center[0]
        y = self.center[1]
        
        while(y < self.radius):
            y+=1
        while(x < self.radius):
            x += 1
        
        if(self.GoingRight == False):
            if((y >= self.radius) and (x >= self.radius)):
                
                x -= self.change_in_x
                y += self.change_in_y
                self.center = (x, y)
                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
            

        else:
            if(y <= self.height - self.radius and x <= self.length - self.radius):
                
                x += self.change_in_x
                y += self.change_in_y
                self.center = (x, y)
                
                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
                
            
        

def main():
    screen = pygame.display.set_mode((length, height))
    second_color = BouncingBall(25, 640, 480)
    second_color.MakeBall(screen, colors)
    first_color = BouncingBall(25, 640, 480)
    first_color.MakeBall(screen, colors)
    third_color = BouncingBall(15, 640, 480)
    third_color.MakeBall(screen, colors)
    
    
    
    while 1:
        screen.fill(colors[4])
        
        second_color.MovingBall(screen, colors)
        first_color.MovingBall(screen, colors)
        third_color.MovingBall(screen, colors)
       
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        msElapse = clock.tick(FPS)
        pygame.display.update()
        
        
        
        
        
main()




        
