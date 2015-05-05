import pygame
from pygame import *
import random
import sys

pygame.init()
mixer.init()
clock = pygame.time.Clock()
#set the length and height of the screen to variables as to make them easier to change
#the screen itself later on
length = 640
height = 480

#the frames per second will check the rate at which the balls will be moving at
FPS = 200

#creating different colors as to use later
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)

#making a dictionay to store these values as to use them later in the code
colors = {0 : red, 1 : green, 2 : blue, 3 : darkBlue, 4 : black, 5 : white, 6 : pink}

class BouncingBall:
    #the constructor will set each object's own unique characteristic in the
    #map that is displayed
    def __init__(self, radius, length, height):
        self.radius = radius
        self.length = length
        self.height = height

        self.startingx = random.randint(self.radius, self.length - self.radius) #this will set the objects starting position that range from the balls radius to the size of the screen
        self.startingy = random.randint(self.radius, self.height - self.radius)

        #what these two will do will be to set the slope the ball will have as it bounces around the box
        self.change_in_x = random.randint(1, 15)
        self.change_in_y = random.randint(1, 10)

        #sets the center point of the circle object
        self.center = (self.startingx, self.startingy)

        self.FPS = FPS  #sets the frames-per-second that each ball object will have

        #the two bool variables are used to check the direction that the ball object is heading
        #it also adds some more realistic features to a ball moving
        self.GoingDown = True
        self.GoingRight = True

        #these booleans are used to check whether the ball has hit one of the four walls in the board
        self.HitRightCorner = False
        self.HitLeftCorner = False
        self.HitTopCorner = False
        self.HitButtomCorner = False

    #
    #this function is incharge of making the ball object with its own unique characteristics
    def MakeBall(self, screen, colors):
        #the color of the ball is set to a default value of green from the dictionary
        pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
        pygame.display.update()


    def playSound(self):
        mixer.music.load('blip.ogg')
        mixer.music.play()


    def MovingBall(self, screen, colors):
        #the temp value are used to check the direction that the ball object is moving so
        self.temp_x = self.center[0]
        self.temp_y = self.center[1]
        #the x and y are used to retrieve the current position of the ball object
        x = self.center[0]
        y = self.center[1]

        #this if statements will determine whether the ball object has hit the buttom
        #of the board
        if(y >= self.height - self.radius):
            self.HitTopCorner = False
            self.HitButtomCorner = True
            self.HitRightCorner = False
            self.HitLeftCorner = False

        #this if statement will check as to whether the ball object has hit the top of the board
        if(y <= self.radius):
            self.HitButtomCorner = False
            self.HitTopCorner = True
            self.HitLeftCorner = False
            self.HitRightCorner = False
        #this wil determine whether the ball object has hit the right side of the board
        if(x >= self.length - self.radius):
            self.HitLeftCorner = False
            self.HitRightCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False

        #this will check whether the ball object has hit the left side of the board
        if(x <= self.radius):
            self.HitRightCorner = False
            self.HitLeftCorner = True
            self.HitTopCorner = False
            self.HitButtomCorner = False


        self.CheckTheWallHit(screen, colors) #this function checks the directio the ball is heading and will call
                                            #functions that relate to those specific locations on the grid
        self.UpdateDirection()      #this function will update the direction of the ball object


    def UpdateDirection(self):  #this function will update the direction in which the ball is heading

        x = self.center[0]
        y = self.center[1]

        if(self.temp_x < x and self.temp_y > y): #this condition checks to see whether the ball is moving to down and to the right
            self.GoingRight = True
            self.GoingDown = True

        elif(self.temp_x > x and self.temp_y > y):#this condition checks to see whether the ball is moving down and to the left
            self.GoingRight = False
            self.GoingDown = True
        elif(self.temp_x < x and self.temp_y < y): #this condition checks to see whether the ball is moving up and to the right
            self.GoingRight = True
            self.GoingDown = False
        else:                                   #else, the ball is moving up and to the left
            self.GoingRight = False
            self.GoingDown = False

    def CheckTheWallHit(self, screen, colors): #in the first runs of the function, the function will go to the last condition

        if(self.HitButtomCorner == True):   #the ball object has hit the buttom of the screen
            self.hitButtomSide(screen, colors)

        elif(self.HitRightCorner == True):  #the ball object has hit the right of the screen
            self.hitRightSide(screen, colors)

        elif(self.HitLeftCorner == True):   #the ball object has hit the left of the screen
            self.hitLeftSide(screen, colors)

        elif(self.HitTopCorner == True):    #the ball object has hit the top of the screen
            self.hitTopSide(screen, colors)

        else:
            self.jumpingAround(screen, colors) #the ball has not hit nay of them and is heading to the right and down

    def jumpingAround(self, screen, colors):    #this function will make the ball move to the right and buttom
        x = self.center[0]
        y = self.center[1]

        if((y <= self.height - self.radius) and (x <= self.length - self.radius)): #this condition checks to see that the ball is within the range of the screen
                                                                                    #as to make sure that the ball does not go outside the screen

            x += self.change_in_x        #it will then update the new position of the ball object with the random slope it has
            y += self.change_in_y
            self.center = (x, y)

            pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)  #it will then go and redraw the circle again but at a new position

    def hitButtomSide(self, screen, colors):
        x = self.center[0]
        y = self.center[1]
        if(self.GoingRight == True):    #this if statement is used to determine the direction that the ball is heading as to determine whether to add
                                        # or subtract for the change in direction
            if((y > self.radius) and (x <= self.length - self.radius)): #this condition will check to see that the ball is within the range of the screen

                y -= self.change_in_y
                x += self.change_in_x
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)

        else:   #if it did not meet the previous requirement, then it is heading to the left

            if((y >= self.radius) and ( x <= self.length - self.radius)):

                y -= self.change_in_y
                x -= self.change_in_x
                self.center = (x, y)
                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)

        self.playSound()

    def hitRightSide(self, screen, colors):
        x = self.center[0]
        y = self.center[1]

        if(self.GoingDown == False): #this condition checks to see whether the ball is going down when it hits the right wall
                                    #if it did, then it will
            if((x >= self.radius) and ((y <= self.height - self.radius) and ( y >= self.radius))):  #this will check to make sure that the ball is within the range of the screen

                x -= self.change_in_x
                y += self.change_in_y
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)

        else:   #if it is not going down, then it subtract the change_in_y value from the center of the circle
            if((x >= self.radius) and ((y <= self.height - self.radius) and ( y >= self.radius))):

                x -= self.change_in_x
                y -= self.change_in_y
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)

    def hitLeftSide(self, screen, colors): #this statement is called when the ball object is hitting the left side of the screen
        x = self.center[0]
        y = self.center[1]

        if(self.GoingDown == False): #checks to see whether the ball is going downn when it hit the left side of the screen
            if(x <= self.length - self.radius and (y >= self.radius and y <= self.height - self.radius)):

                x += self.change_in_x
                y += self.change_in_y
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)

        else: #if it did not meet the previous requirement, then it will add the change_in_x value to the current value of the circle
            if((x <= self.length - self.radius) and ((y >= self.radius) and (y <= self.height - self.radius))):

                x += self.change_in_x
                y -= self.change_in_y
                self.center = (x, y)

                pygame.draw.circle(screen, colors[1], self.center, self.radius, 0) #it then redraws the circle, but in its new position


    def hitTopSide(self, screen, colors):   #this function called when the ball has hit the top of the screen
        x = self.center[0]
        y = self.center[1]

        if (y < self.radius): #this loop is used to make sure that the value of x does not
            y = self.radius
        if(x < self.radius):
            x = self.radius

        if(self.GoingRight == False):   #this checks to see the direction in which the ball is coming from and will add the change_in_y to the y variable
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
    screen = pygame.display.set_mode((length, height)) #this will create the screen with the size determined by the length and height
    second_color = BouncingBall(25, 640, 480)   #this will create a ball object and initialize its size and the dimensions of the screen
    second_color.MakeBall(screen, colors)   #this will draw the ball object on the screen with a given color
    first_color = BouncingBall(25, 640, 480)#this will create a ball object and initialize its size and the dimensions of the screen
    first_color.MakeBall(screen, colors) #this will draw the ball object on the screen with a given color
    third_color = BouncingBall(15, 640, 480) #this will create a ball object and initialize its size and the dimensions of the screen
    third_color.MakeBall(screen, colors) #this will draw the ball object on the screen with a given color



    while 1:
        screen.fill(colors[4])  #this will fill in the screen with a background color depending on the dictionary
        msElapse = clock.tick(FPS)  #this is used to slow down the time in which the code runs
        second_color.MovingBall(screen, colors) #the object calls the function that will determine in which direction the ball will move
        first_color.MovingBall(screen, colors)
        third_color.MovingBall(screen, colors)

        for event in pygame.event.get():    #this loop is used to check whether the user has closed the pygame window
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()

        pygame.display.update()

main()
