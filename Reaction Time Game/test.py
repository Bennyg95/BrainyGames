import pygame
from pygame import *
import random
import sys


pygame.init()
mixer.init()
clock = pygame.time.Clock()

length = 640
height = 480

FPS = 10
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
        self.index = 1

        self.startingx = random.randint(self.radius, self.length - self.radius)
        self.startingy = random.randint(self.radius, self.height - self.radius)

        self.change_in_x = random.randint(1, 15)
        self.change_in_y = random.randint(1, 10)

        self.center = (self.startingx, self.startingy)
        self.x = self.center[0]
        self.y = self.center[1]

        #self.FPS = random.randint(200, 2000)
        self.FPS = 500
        self.GoingDown = True
        self.GoingRight = True

        self.HitRightCorner = False
        self.HitLeftCorner = False
        self.HitTopCorner = False
        self.HitButtomCorner = False

        self.got_pressed = False
        self.got_unpressed = False

    def isClicked(self, mouse_position_x, mouse_position_y):

        if((mouse_position_x > abs(self.x - self.radius) and mouse_position_x < abs(self.x + self.radius)) and ((mouse_position_y > abs(self.x - self.radius) and mouse_position_y < abs(self.x + self.radius)))):

            if(pygame.mouse.get_pressed() == (1, 0, 0)):
                self.got_pressed = True
                self.got_unpressed = False

            elif(pygame.mouse.get_pressed() == (0, 0, 1)):
                self.got_unpressed = True
                self.got_pressed = False

            if(self.got_pressed == True and self.got_unpressed == False):
                self.index = 2

            elif(self.got_pressed == False and self.got_unpressed == True):
                self.index = 1




    def MakeBall(self, screen, colors):
        pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
        pygame.display.update()


    def playSound():
        mixer.music.load('blip.ogg')
        mixer.music.play()


    def MovingBall(self, screen, colors, mouse_position_x, mouse_position_y):

        self.temp_x = self.center[0]
        self.temp_y = self.center[1]
        self.x = self.center[0]
        self.y = self.center[1]

        if(self.y >= self.height - self.radius):
            self.HitTopCorner = False
            self.HitButtomCorner = True
            self.HitRightCorner = False
            self.HitLeftCorner = False


        if(self.y <= self.radius):
            self.HitButtomCorner = False
            self.HitTopCorner = True
            self.HitLeftCorner = False
            self.HitRightCorner = False


        if(self.x >= self.length - self.radius):
            self.HitLeftCorner = False
            self.HitRightCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False

        if(self.x <= self.radius):
            self.HitRightCorner = False
            self.HitLeftCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False


        self.CheckDirection(screen, colors)
        self.Direction()
        self.isClicked(mouse_position_x, mouse_position_y)



    def Direction(self):


        if(self.temp_x < self.x and self.temp_y > self.y):
            self.GoingRight = True
            self.GoingDown = True
        elif(self.temp_x > self.x and self.temp_y > self.y):
            self.GoingRight = False
            self.GoingDown = True
        elif(self.temp_x < self.x and self.temp_y < self.y):
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


        if((self.y <= self.height - self.radius) and (self.x <= self.length - self.radius)):


            self.x += self.change_in_x
            self.y += self.change_in_y
            self.center = (self.x, self.y)

            pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)




    def hitButtomSide(self, screen, colors):

        '''
        if( x > self.length - self.radius):
            x = self.length - self.radius
        if(y > self.length - self.radius):
            y = self.length - self.radius
        '''
        if(self.GoingRight == True):
            if((self.y > self.radius) and (self.x <= self.length - self.radius)):

                self.y -= self.change_in_y
                self.x += self.change_in_x
                self.center = (self.x, self.y)

                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

        else:
            if((self.y >= self.radius) and (self.x <= self.length - self.radius)):

                self.y -= self.change_in_y
                self.x -= self.change_in_x
                self.center = (self.x, self.y)
                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)




    def hitRightSide(self, screen, colors):

        '''
        if( x > self.length - self.radius):
            x = self.length - self.radius
        if(y > self.length - self.radius):
            y = self.length - self.radius ###
        '''
        if(self.GoingDown == True):
            if((self.x >= self.radius) and ((self.y <= self.height - self.radius) and (self.y >= self.radius))):

                self.x -= self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)

                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

        else:
            if((self.x >= self.radius) and ((self.y <= self.height - self.radius) and ( self.y >= self.radius))):

                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)



    def hitLeftSide(self, screen, colors):

        if(self.GoingDown == False):
            if(self.x <= self.length - self.radius and (self.y >= self.radius and self.y <= self.height - self.radius)):

                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

        else:
            if((self.x <= self.length - self.radius) and ((self.y >= self.radius) and (self.y <= self.height - self.radius))):

                self.x += self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)

                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)


    def hitTopSide(self, screen, colors):

        while(self.y < self.radius):
            self.y+=1
        while(self.x < self.radius):
            self.x += 1

        if(self.GoingRight == False):
            if((self.y >= self.radius) and (self.x >= self.radius)):

                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)
                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)


        else:
            if(self.y <= self.height - self.radius and self.x <= self.length - self.radius):

                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

                pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)




def main():
    screen = pygame.display.set_mode((length, height))
    second_color = BouncingBall(25, 640, 480)
    second_color.MakeBall(screen, colors)
    #first_color = BouncingBall(25, 640, 480)
    #first_color.MakeBall(screen, colors)
    #third_color = BouncingBall(15, 640, 480)
    #third_color.MakeBall(screen, colors)



    while 1:
        screen.fill(colors[4])
        mouse_position_x = pygame.mouse.get_pos()[0]
        mouse_position_y = pygame.mouse.get_pos()[1]


        second_color.MovingBall(screen, colors, mouse_position_x, mouse_position_y)
        #first_color.MovingBall(screen, colors, mouse_position_x, mouse_position_y)
        #third_color.MovingBall(screen, colors, mouse_position_x, mouse_position_y)

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        msElapse = clock.tick(FPS)
        pygame.display.update()





main()
