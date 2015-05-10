import pygame
from pygame import *
import random
import sys

pygame.init()
mixer.init()
clock = pygame.time.Clock()

length = 640
height = 480
FPS = 50

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
        self.image = pygame.image.load('example.jpg')


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
        if((self.y <= self.height - self.radius and self.y >= self.radius) and (self.x <= self.length - self.radius and self.x >= self.radius)):
            self.x += self.change_in_x
            self.y += self.change_in_y
            self.center = (self.x, self.y)
            #screen.blit(self.image, (self.center[0], self.center[1]))
        else:
            self.x -= self.change_in_x
            self.y -= self.change_in_y
            self.center = (self.x, self.y)
        pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

    def hitButtomSide(self, screen, colors):

        if(self.GoingRight == True):
            if((self.y > self.radius) and (self.x <= self.length - self.radius)):

                self.y -= self.change_in_y
                self.x += self.change_in_x
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))


            else:
                self.y += self.change_in_y
                self.y -= self.change_in_x
                self.center = (self.x, self.y)


        else:
            if((self.y >= self.radius) and (self.x <= self.length - self.radius)):

                self.y -= self.change_in_y
                self.x -= self.change_in_x
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))

            else:

                self.y += self.change_in_y
                self.x += self.change_in_x
                self.center = (self.x, self.y)

        pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

    def hitRightSide(self, screen, colors):
        if(self.GoingDown == True):
            if((self.x >= self.radius) and ((self.y <= self.height - self.radius) and (self.y >= self.radius))):

                self.x -= self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))
            else:
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)


        else:
            if((self.x >= self.radius) and ((self.y <= self.height - self.radius) and ( self.y >= self.radius))):

                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))

            else:
                self.x += self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)

        pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

    def hitLeftSide(self, screen, colors):


        if(self.GoingDown == False):
            if((self.x <= self.length - self.radius) and (self.y >= self.radius and self.y <= self.height - self.radius)):
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))

            else:
                self.x -= self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)

        else:
            if((self.x <= self.length - self.radius) and ((self.y >= self.radius) and (self.y <= self.height - self.radius))):

                self.x += self.change_in_x
                self.y -= self.change_in_y
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))
            else:
                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

        pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

    def hitTopSide(self, screen, colors):
        if(self.GoingRight == False):
            if((self.y <= abs(self.height - self.radius)) and (self.y >= self.radius) and (self.x > self.radius) and (self.x <= abs(self.height - self.radius))):
                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))
            else:
                self.x -= self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

        else:
            if((self.y >= self.radius) and (self.x >= self.radius)):
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)
                #screen.blit(self.image, (self.center[0], self.center[1]))
            else:
                self.x += self.change_in_x
                self.y += self.change_in_y
                self.center = (self.x, self.y)

        pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

def main():
    length = 640
    height = 480
    screen = pygame.display.set_mode((length, height))
    list = []
    x = random.randint(6, 11)
    print x
    #x = 2
    for i in range(x):
        list.append(BouncingBall(25, length, height))
    for ball in range(len(list)):
        list[ball].MakeBall(screen, colors)

    while 1:
        screen.fill(colors[4])
        mouse_position_x = pygame.mouse.get_pos()[0]
        mouse_position_y = pygame.mouse.get_pos()[1]
        for i in range(len(list)):
            list[i].MovingBall(screen, colors)

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        msElapse = clock.tick(FPS)
        pygame.display.update()

main()
