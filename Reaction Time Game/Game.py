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
    def __init__(self, picture_location, radius, length, height, NewImages):
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
        self.image = pygame.image.load(NewImages[picture_location])


        self.GoingDown = True
        self.GoingRight = True

        self.HitRightCorner = False
        self.HitLeftCorner = False
        self.HitTopCorner = False
        self.HitButtomCorner = False

    def MakeBall(self, screen):

        #pygame.draw.circle(screen, colors[1], self.center, self.radius, 0)
        screen.blit(self.image, (self.center[0], self.center[1]))
        pygame.display.update()


    def playSound():
        mixer.music.load('blip.ogg')
        mixer.music.play()


    def MovingBall(self, screen):

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

        self.CheckDirection(screen)
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

    def CheckDirection(self, screen):
        if(self.HitButtomCorner == True):
            self.hitButtomSide(screen)

        elif(self.HitRightCorner == True):
            self.hitRightSide(screen)

        elif(self.HitLeftCorner == True):
            self.hitLeftSide(screen)

        elif(self.HitTopCorner == True):
            self.hitTopSide(screen)

        else:
            self.jumpingAround(screen)



    def jumpingAround(self, screen):
        if((self.y <= self.height - self.radius and self.y >= self.radius) and (self.x <= self.length - self.radius and self.x >= self.radius)):
            self.x += self.change_in_x
            self.y += self.change_in_y
            self.center = (self.x, self.y)
            #screen.blit(self.image, (self.center[0], self.center[1]))
        else:
            self.x -= self.change_in_x
            self.y -= self.change_in_y
            self.center = (self.x, self.y)

        #pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)
        screen.blit(self.image, (self.center[0], self.center[1]))
    def hitButtomSide(self, screen):

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
        screen.blit(self.image, (self.center[0], self.center[1]))
        #pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

    def hitRightSide(self, screen):
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
        screen.blit(self.image, (self.center[0], self.center[1]))
        #pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

    def hitLeftSide(self, screen):


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
        screen.blit(self.image, (self.center[0], self.center[1]))
        #pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

    def hitTopSide(self, screen):
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

        screen.blit(self.image, (self.center[0], self.center[1]))
        #pygame.draw.circle(screen, colors[self.index], self.center, self.radius, 0)

def getPixelArray(filename):
    """ Open file, load image and convert it to 3D pixel array. """
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message

    return pygame.surfarray.array3d(image)

def saveSurface(pixels, filename):
    """ Convert 3D array of pixels to Pygame surface and save. """
    try:
        surf = pygame.surfarray.make_surface(pixels)
    except IndexError:
        pixels = (width, height, colours)
        surf = pygame.display.set_mode((width, height))
        pygame.surfarray.blit_array(surf, pixels)

    pygame.image.save(surf, filename)

def main():
    length = 640
    height = 480
    screen = pygame.display.set_mode((length, height))
    list = []
    x = random.randint(4, 8)
    while(x % 2 != 0):
        x = random.randint(4, 8)

    OriginalPictures = []
    Images = []
    SplitImagesArray = []
    NewImages = []

    First_picture = getPixelArray('example.jpg')
    Second_picture = getPixelArray('puppy.jpg')
    Third_picture = getPixelArray('Golden Gate Bridge.jpg')
    Fourth_picture = getPixelArray('Family_picture.jpg')

    OriginalPictures.append(First_picture)
    OriginalPictures.append(Second_picture)
    OriginalPictures.append(Third_picture)
    OriginalPictures.append(Fourth_picture)

    Images.append('example.jpg')
    Images.append('puppy.jpg')
    Images.append('Golden Gate Bridge.jpg')
    Images.append('Family_picture.jpg')


    #temp1 = pygame.surfarray.make_surface(Original)
    for i in range(len(OriginalPictures)):

        LoadImage = pygame.image.load(Images[i])
        ImageDimension = LoadImage.get_rect().size
        temp1 = OriginalPictures[i][ImageDimension[0]/2: , : , :]
        temp2 = OriginalPictures[i][ :ImageDimension[1]/2, :, : ]
        AlteredImage1 = pygame.surfarray.make_surface(temp1)
        AlteredImage2 = pygame.surfarray.make_surface(temp2)

        AlteredImage1 = pygame.transform.scale(AlteredImage1, (100, 100))
        AlteredImage2 = pygame.transform.scale(AlteredImage2, (100, 100))

        SplitImagesArray.append(AlteredImage1)
        SplitImagesArray.append(AlteredImage2)

    #surf = pygame.surfarray.make_surface(AlteredImage1)
    #pygame.image.save(SplitImagesArray[0], 'Puppy1.jpg')
    pygame.image.save(SplitImagesArray[0], 'Flower1.jpg')
    pygame.image.save(SplitImagesArray[1], 'Flower2.jpg')
    pygame.image.save(SplitImagesArray[2], 'Puppy1.jpg')
    pygame.image.save(SplitImagesArray[3], 'Puppy2.jpg')
    pygame.image.save(SplitImagesArray[4], 'GoldenBridge1.jpg')
    pygame.image.save(SplitImagesArray[5], 'GoldenBridge2.jpg')
    pygame.image.save(SplitImagesArray[6], 'Family_picture1.jpg')
    pygame.image.save(SplitImagesArray[7], 'Family_picture2.jpg')

    NewImages.append('Flower1.jpg')
    NewImages.append('Flower2.jpg')
    NewImages.append('Puppy1.jpg')
    NewImages.append('Puppy2.jpg')
    NewImages.append('GoldenBridge1.jpg')
    NewImages.append('GoldenBridge2.jpg')
    NewImages.append('Family_picture1.jpg')
    NewImages.append('Family_picture2.jpg')


    for i in range(x):
        list.append(BouncingBall(i, 50, length, height, NewImages))
    for ball in range(len(list)):
        list[ball].MakeBall(screen)
    Ready = False
    while (Ready == False):
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        screen.fill((255, 0, 255))

    while 1:
        screen.fill((0, 0, 0))
        mouse_position_x = pygame.mouse.get_pos()[0]
        mouse_position_y = pygame.mouse.get_pos()[1]
        for i in range(len(list)):
            list[i].MovingBall(screen)

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
        msElapse = clock.tick(FPS)
        pygame.display.update()

main()
