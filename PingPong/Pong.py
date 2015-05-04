import pygame

######################################################################################
class Player():
######################################################################################

	def __init__(self):
		self.x, self.y = 16, SCREENHEIGHT/2     #initial position of player
		self.speed = 3  #speed at which the player will be moving
		self.padWidth, self.padHeight = 8, 64   #size of the player
		self.score = 0  #initial score will be zero

	##################################################################################
	def playerScore(self):
	##################################################################################
		#out put score on the screen
		scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
		screen.blit(scoreBlit, (32, 16))

		#output winner
		if self.score == 10:    # ones player reaches 10
			print "player 1 wins!"  #output winner
			exit()  #end program

	##################################################################################
	def movePlayer(self):
	##################################################################################
		keys = pygame.key.get_pressed() #Gets key been pressed

		if keys[pygame.K_w]:   # when key 'w' is pressed
			self.y -= self.speed    # move the player down

		elif keys[pygame.K_s]:  #when key 's' is pressed
			self.y += self.speed    #move player up
	
		if self.y <= 0: 
			self.y = 0
		elif self.y >= SCREENHEIGHT-64:
			self.y = SCREENHEIGHT-64
	
	##################################################################################
	def drawPlayer(self):
	##################################################################################
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWidth, self.padHeight))

######################################################################################
class Enemy():
######################################################################################
	def __init__(self):
	##################################################################################
		self.x, self.y = SCREENWITH-16, SCREENHEIGHT/2
		self.speed = 3
		self.padWidth, self.padHeight = 8, 64
		self.score = 0
		#self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
	
	##################################################################################
	"""def enemyScore(self):
	##################################################################################
		scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
		screen.blit(scoreBlit, (SCREENHEIGHT+92, 16))
		if self.score == 10:
			print "Player 2 wins!"
			exit()"""
	##################################################################################
	def moveEnemy(self):
	##################################################################################
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.y -= self.speed
		elif keys[pygame.K_DOWN]:
			self.y += self.speed
	
		if self.y <= 0:
			self.y = 0
		elif self.y >= SCREENHEIGHT-64:
			self.y = SCREENHEIGHT-64
	
	##################################################################################
	def drawEnemy(self):
	##################################################################################
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWidth, self.padHeight))

######################################################################################
class Ball():
######################################################################################
	def __init__(self):
	##################################################################################
		self.x, self.y =    SCREENWITH/2, SCREENHEIGHT/4
		self.speed_x = -3 	#ball moves in a negative direction on the x axis
		self.speed_y = 3 	# ball moves positively on the y axis
		self.size = 8	# size of the ball
	
	##################################################################################
	def moveBall(self):
	##################################################################################
		self.x += self.speed_x # KEEPS THE BALL MOVING
		self.y += self.speed_y	# 

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
	##################################################################################
	def drawBall(self):
	##################################################################################
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))


SCREENWITH, SCREENHEIGHT = 640,480

screen = pygame.display.set_mode((SCREENWITH, SCREENHEIGHT))

clock = pygame.time.Clock()

FPS = 60

ball = Ball()
player = Player()
enemy = Enemy()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print "Exited"
			exit()

	ball.moveBall()
	player.movePlayer()
	enemy.moveEnemy()

	screen.fill((0,0,0))

	ball.drawBall()
	player.drawPlayer()
	enemy.drawEnemy()

	pygame.display.flip()
	clock.tick(FPS)
