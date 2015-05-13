import pygame
from pygame import *
import sys



#import Classes
#import process


pygame.init()

from BrainyGames.SpaceBugs import Main
	
def main():	
	length = 640
	height = 480
	screen = pygame.display.set_mode((length, height))
	Ready = False
	pygame.display.set_caption("Basic Pygame Program")
	while (Ready == False):
		for event in pygame.event.get():
					if event.type == pygame.QUIT:
					   pygame.quit()
					   sys.exit()
		background = pygame.Surface(screen.get_size())
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, (255, 255, 255), (150, height/2, 300, 100))

		font = pygame.font.Font(None, 36)
		text = font.render("Let's Start", 1, (255, 0, 0))
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx - 20
		textpos.centery = background.get_rect().centery + 50
		screen.blit(text, textpos)
		text = font.render("Welcome", 1, (255, 255, 255))
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx
		screen.blit(text, textpos)
		text = font.render("This game is designed to test your ability", 1 ,(255, 255, 255))
		textpos = text.get_rect()
		textpos.centery = background.get_rect().centery - 100
		textpos.centerx = background.get_rect().centerx
		screen.blit(text, textpos)
		text = font.render("to recognize a picture when split in two pieces", 1, (255, 255, 255))
		textpos = text.get_rect()
		textpos.centery = background.get_rect().centery - 70
		textpos.centerx = background.get_rect().centerx
		screen.blit(text, (textpos))

		mouse_position_x = pygame.mouse.get_pos()[0]
		mouse_position_y = pygame.mouse.get_pos()[1]

		if(mouse_position_x > 200 and mouse_position_x < 500 and mouse_position_y > 240 and mouse_position_y < 340):
			if(pygame.mouse.get_pressed() == (1, 0, 0)):
				Ready = True
				MinionGame()

			else:
				Ready = False
		pygame.display.update()

main()