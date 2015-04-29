
import pygame

class Ball():
    def __init__(self):
        self.x, self.y =    SCREENWITH/2, SCREENHEIGHT/4
        self.speed_x = -3
        self.speed_y = 3
        self.size = 8
    
    def movement(self):
        self.x += self.speed_x # KEEPS THE BALL MOVING
        self.y += self.speed_y

        #WHEN COLLIDING WITH A WALL
        if self.y <= 0:
            self.speed_y *= -1
        elif self.y >= SCREENHEIGHT-self.size:
            self.speed_y *= -1

        if self.x <= 0:
            self.__init__()

        elif self.x >= SCREENWITH-self.size:
            self.__init__()
            self.speed_x = 3

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))


SCREENWITH, SCREENHEIGHT = 640,480

screen = pygame.display.set_mode((SCREENWITH, SCREENHEIGHT))

clock = pygame.time.Clock()

FPS = 60

ball = Ball()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print "Exited"
			exit()

	ball.movement()

	screen.fill((0,0,0))

	ball.draw()

	pygame.display.flip()
	clock.tick(FPS)
