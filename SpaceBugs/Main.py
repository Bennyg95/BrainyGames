import pygame, sys			#imports pygame and the system
from Classes import *		# imports Classes file
from process import process	#imports process file

pygame.init()			#initializes pygame
pygame.mixer.init()	# for music

SCREENWIDTH, SCREENHEIGHT = 740, 510	#sets value for screen width and height
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))	# Initializes screen with its size
clock = pygame.time.Clock()		#game will run along with clock
FPS = 24	#Frames per second
total_frames = 0;	#iniializes frames

background = pygame.image.load("images/space1.png")		#creates a background

img = pygame.image.load("minions/shootingminion.png")	# load picture for the minion that will be shooting
imHeight, imWidth = img.get_rect().size #gets the size of the image

minion = Minion(0, SCREENHEIGHT - imHeight, "minions/shootingminion.png")	# gets image of minion

pygame.mixer.music.load("music/pirates.mp3")		# background music
pygame.mixer.music.play()		# plays the song

# ----------Main Program Loop --------------------
while True:


########################################################################
# LOGIC
########################################################################
	process(minion, FPS, total_frames)				# calls the process method passes minion 

	minion.motion(SCREENWIDTH, SCREENHEIGHT)		# sets motion to minion
	EvilMinion.update_all(SCREENWIDTH, SCREENHEIGHT)		#will update game
	MinionProjectile.movement()						# moves projectiles
	total_frames += 1								#addes frames
	
########################################################################

########################################################################
# DRAW
########################################################################
	screen.blit(background, (0,0))					#outputs background
	BaseClass.allsprites.draw(screen)				#draws all sprites
	MinionProjectile.List.draw(screen)				#draws list of projectiles
########################################################################
	
	pygame.display.flip()	

	clock.tick(FPS)	#time in Frames per second

