import random # we need a random generator for shapes and colors.
import time
import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 15 #Frames Per Second.
WINDOWWIDTH = 640  #Game screen width
WINDOWHEIGHT = 480 #Game screen height
REVEALSPEED = 5 #Speed to reveal the box chosen by the player. 5 Frames per second
BOARDWIDTH = 2 #How many columns of boxes we will have.
BOARDHEIGHT = 3 #How many roms of boxes we will have.
#Check that there is an even number of boxxes so we are able to make pairs.
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
BOXSIZE = 50 #Size of the boxes that will be covering the pistures.
GAPSIZE = 25 #The Gap between the boxes.

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2) #This makes the the game be in the center of the game.
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#Colors for the shapes.
GRAY =     (100, 100, 100)
DARKGRAY = ( 60,  60,  60)
WHITE =    (255, 255, 255)
BLUE =     (  0,   0, 255)
YELLOW =   (255, 255,   0)
ORANGE =   (255, 128,   0)
PURPLE =   (255,   0, 255)


#Extxra color for the background, boxes, etc.

BGCOLOR = PURPLE
LIGHTBGCOLOR = YELLOW
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

#Actual shapes. 
DONUT = 'Donut'
SQUARE = 'Square'
DIAMOND = 'Diamond'
LINES = 'Lines'
OVAL = 'Oval'


ALLCOLORS = (BLUE, ORANGE, YELLOW, GRAY) # so it contains all of the colors.
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)#COntains all shapes.
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT #Makes sure the borad is bigger than the shapes/colors defined.

def main():
    global FPSCLOCK, WINDOWSURF #Global varibales that will be used inside the main.
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    WINDOWSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1, 0.1)

    mousex = 100#Where our mouse will start when we run the program.
    mousey = 100
    pygame.display.set_caption('The Memory Game')#Caption for the window

    mainBoard = getRandomizedBoard()#Calls function to make the combinations, pairs, and randomely puts them in different places.
    revealedBoxes = generateRevealedBoxesData(False)#Calls function ...which starts false, so it shows them for a bit.

    firstSelection = None

    WINDOWSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: # main game loop
        mouseClicked = False

        WINDOWSURF.fill(BGCOLOR) # drawing the window
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = isOverBox(mousex, mousey)
        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            drawHighlightBox(boxx, boxy)
            if mouseClicked and not revealedBoxes[boxx][boxy]:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)], REVEALSPEED)
                revealedBoxes[boxx][boxy] = True # set the box as "revealed"

                if firstSelection == None: # this was the first box clicked
                    firstSelection = (boxx, boxy)
                else: # this was the second box clicked
                    # Check if there is a match between the two boxes.
                    shape1, color1 = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    shape2, color2 = getShapeAndColor(mainBoard, boxx, boxy)

                    if shape1 != shape2 or color1 != color2:
                        # Icons don't match. Cover up both selections.
                        time.sleep(0.5)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)], REVEALSPEED)
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        time.sleep(1)

                        # Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        time.sleep(1)

                        # Replay the start game animation.
                        startGameAnimation(mainBoard)
                    firstSelection = None # reset the firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def splitIntoGroupsOf(groupSize, theList):
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i+groupSize])
    return result


def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)#Show the covered boxes.
    boxes = []
    for x in range(BOARDWIDTH):         #Go through all the boxes.
        for y in range(BOARDHEIGHT):
            boxes.append( (x, y) ) #..and show them
    random.shuffle(boxes)#shuffle the bboxed
    boxGroups = splitIntoGroupsOf(8, boxes)

    for boxGroup in boxGroups:
        drawBoard(board, coveredBoxes)
        revealBoxesAnimation(board, boxGroup, REVEALSPEED)
        coverBoxesAnimation(board, boxGroup, REVEALSPEED)


def gameWonAnimation(board):
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        WINDOWSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        time.sleep(0.3)


def hasWon(revealedBoxes):
    for i in revealedBoxes:
        if False in i:
            return False # return False if any boxes are covered.
    return True


def getShapeAndColor(board, boxx, boxy):
    return board[boxx][boxy][0], board[boxx][boxy][1]


def revealBoxesAnimation(board, boxesToReveal, speed):
    # Do the "box reveal" animation.
    for coverage in range(BOXSIZE, (-speed) - 1, -speed):
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover, speed):
    # Do the "box cover" animation.
    for coverage in range(0, BOXSIZE + speed, speed):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoxCovers(board, boxes, coverage):
    # Draws boxes being covered/revealed.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(WINDOWSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawShape(shape, color, box[0], box[1])
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(WINDOWSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = []
    for color in ALLCOLORS: #for loop to go through all colors
        for shape in ALLSHAPES:# ....and through all the shapes.
            icons.append( (shape, color) )# Makes sure it creates every possible combination for the shapes and the colors.

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) #There should be different combination of shapes and colors for the amount of boxes.
    icons = icons[:numIconsUsed] * 2 #Make a copy of the first icon(remember we want pairs.)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH): #loop for the width 
        columns = []
        for y in range(BOARDHEIGHT):#..and height
            randomIndex = random.randint(0, len(icons) - 1)#RAndomize where the shapes will go.
            columns.append(icons[randomIndex])
            del icons[randomIndex] # remove the icons as we assign them
        board.append(columns)#make it happen.
    return board


def leftTopCoordsOfBox(boxx, boxy):
    # See how big the margins are for each side.
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def drawBoard(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(WINDOWSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawShape(shape, color, boxx, boxy)


def isOverBox(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(WINDOWSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


def drawShape(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    half =    int(BOXSIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    if shape == DONUT:
        pygame.draw.circle(WINDOWSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(WINDOWSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(WINDOWSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(WINDOWSURF, color, (left, top + i), (left + i, top))
    elif shape == OVAL:
        pygame.draw.ellipse(WINDOWSURF, color, (left, top + quarter, BOXSIZE, half))


if __name__ == '__main__':
    main()
