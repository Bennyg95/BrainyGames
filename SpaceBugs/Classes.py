import pygame, math
from random import randint

##############################################################################################
class BaseClass(pygame.sprite.Sprite):	#contains every single sprite in the game
##############################################################################################
	
	allsprites = pygame.sprite.Group() #all  ojects that are created 
	# __init__(self, x, y,  image_string):
##############################################################################################
	def __init__(self, x, y, image_string):
##############################################################################################

		pygame.sprite.Sprite.__init__(self) #initializes an object
		BaseClass.allsprites.add(self)	#adds the object to the all sprites list

		self.image = pygame.image.load(image_string) #variable to save an image
		
		self.rect = self.image.get_rect() #gets the dimentions of the image to the rectangle
		self.rect.x = x	# width of an object
		self.rect.y = y	# height of an object

	def destroy(self, ClassName):	#function that will destroy the object

		ClassName.List.remove(self)	#removes the object from the list
		BaseClass.allsprites.remove(self)	#removes the object form the list of sprites
		del self	#deletes the object

##############################################################################################
class Bug(BaseClass):
##############################################################################################

	List = pygame.sprite.Group()	#sets list to the sprite group
	going_right = True	# bugs will move to the right

	def __init__(self, x, y,  image_string):	#initializes a function	
		BaseClass.__init__(self, x, y, image_string)	#Initializes the baseclass
		Bug.List.add(self)	# adds bug created to the List
		self.velx, self.vely = 0, 8	# sets sets corresponding velocities
		self.jumping, self.go_down = False, False	# sets jumpint and and go dows to false

	def motion(self, SCREENWIDTH, SCREENHEIGHT):	#sets motion function
		predicted_location = self.rect.x + self.velx	# predicts the next location

		if predicted_location < 0:	# if predicted location is out of the screen
			self.velx = 0	# stops moving
		elif predicted_location + self.rect.width > SCREENWIDTH:	#if predicted location is out of the screen
			self.velx = 0	# stop moving

		self.rect.x += self.velx	# keeps bug moving

		self.__jump(SCREENHEIGHT)	#call the jump function

	def __jump(self, SCREENHEIGHT):	# defines the jump function
		max_jump = 75	# max height = 75

		if self.jumping:	# if ub is jumping
			if self.rect.y < max_jump:	# if current height is less than the max height
				self.go_down = True	# sets go down to true
			if self.go_down:	# if bug is going down
				self.rect.y += self.vely	# add the height of bug

				predicted_location = self.rect.y + self.vely

				if predicted_location + self.rect.height> SCREENHEIGHT:
					self.jumping = False
					self.go_down = False
			else:
				self.rect.y -= self.vely

##############################################################################################
class Enemy(BaseClass):
##############################################################################################
	List = pygame.sprite.Group()
	def __init__(self, x, y, image_string):
		BaseClass.__init__(self, x, y, image_string)
		Enemy.List.add(self) # adds enemies to list
		self.health = 100

		self.velx, self.vely= randint(1, 4), 2 # 1 to 4 pixels per second
		self.amplitude, self.period = randint(20, 140), randint(4, 5) / 100.0

	@staticmethod
	def update_all(SCREENWIDTH, SCREENHEIGHT):
		for enemy in Enemy.List:
			if enemy.health <= 0:
				enemy.velx = 0
				if enemy.rect.y + enemy.rect.height < SCREENHEIGHT:
					enemy.rect.y += enemy.vely
			else:
				enemy.fly(SCREENWIDTH)


	def fly(self, SCREENWIDTH):

		if self.rect.x + self.rect.width > SCREENWIDTH or self.rect.x < 0:
			self.image = pygame.transform.flip(self.image, True, False) # flips horizontally
			self.velx =-self.velx

		self.rect.x += self.velx
		# a * sin(bx + c ) + y sets a wave and an aplitude for movement
		self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) + 200 #vertical movement

	@staticmethod 
	def movement(SCREENWIDTH):
		for enemy in Enemy.List:
			enemy.fly(SCREENWIDTH)

##############################################################################################
class BugProjectile(pygame.sprite.Sprite):
##############################################################################################
	List = pygame.sprite.Group()

	normal_list = []
	fire = True

	def __init__(self, x, y, if_fire, image_string):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image_string)

		self.rect = self.image.get_rect() #gets the dimentions of the image to the rectangle
		self.rect.x = x
		self.rect.y = y
		self.if_fire = if_fire
		self.rect.width

		try:
			last_element = BugProjectile.normal_list[-1]
			difference = abs(self.rect.x - last_element.rect.x)

			if difference < self.rect.width:
				return 
		except Exception:
			pass

		BugProjectile.normal_list.append(self)
		BugProjectile.List.add(self)
		self.velx = None

	@staticmethod
	def movement():
		for projectile in BugProjectile.List:
			projectile.rect.x += projectile.velx

	def destroy(self):
		BugProjectile.List.remove(self)
		BugProjectile.normal_list.remove(self)
		del self



