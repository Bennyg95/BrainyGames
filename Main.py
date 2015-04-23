import pygame, sys
from Classes import *
from process import process

pygame.init()
pygame.mixer.init()	# for music

SCREENWIDTH, SCREENHEIGHT = 740, 510
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
FPS = 24
total_frames = 0;

background = pygame.image.load("images/space1.png")

img = pygame.image.load("images/bug1.png")
imHeight, imWidth = img.get_rect().size

bug = Bug(0, SCREENHEIGHT - imHeight, "images/bug1.png")

pygame.mixer.music.load("music/pirates.mp3")
pygame.mixer.music.play()

# ----------Main Program Loop --------------------
while True:


########################################################################
# LOGIC
########################################################################
	process(bug, FPS, total_frames)

	bug.motion(SCREENWIDTH, SCREENHEIGHT)
	Enemy.update_all(SCREENWIDTH, SCREENHEIGHT)
	BugProjectile.movement()
	total_frames += 1
	
########################################################################

########################################################################
# DRAW
########################################################################
	screen.blit(background, (0,0))	
	BaseClass.allsprites.draw(screen)
	BugProjectile.List.draw(screen)
########################################################################
	
	pygame.display.flip()

	clock.tick(FPS)

