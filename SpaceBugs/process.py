




import pygame, sys, Classes, random	#imports pygame, system, Classes and random
##############################################################################################
def process(minion, FPS, total_frames):	
##############################################################################################

	for event in pygame.event.get():	
		if event.type == pygame.QUIT:	#if game is terminated
			pygame.quit()	#quit pygame
			sys.exit()	#exit the system

		if event.type == pygame.KEYDOWN:	#pressing down on a key
			if event.key == pygame.K_e:	 	#if that key is e
				Classes.MinionProjectile.fire = not Classes.MinionProjectile.fire 	#negate fire

	keys = pygame.key.get_pressed()	#gets key been pressed

	if keys[pygame.K_d]: # d key
		Classes.Minion.going_right = True	# Moves to the right
		minion.image = pygame.image.load("minions/shootingminion.png")	# loads image for minion
		minion.velx = 5	# sets velocity for minion
	elif keys[pygame.K_a]:	# a key
		Classes.Minion.going_right = False	# moves to the left
		minion.image = pygame.image.load("minions/shootingminion2.png")	# loads image of minion rotated
		minion.velx = -5	# moves minion in a negative position
	else:
		minion.velx = 0	# stops moving

	if keys[pygame.K_w]:	# w key
		minion.jumping = True		#makes it jump

	if keys[pygame.K_SPACE]:	#space key
		######################################################################################
		def direction():	
		######################################################################################
			if Classes.Minion.going_right: 	#if minion is moving right
				p.velx = 8		# velocity 8
			else:
				#p.image = pygame.transform.flip(p.image, True, False)
				p.velx = -8	 	# move to the left

		if(Classes.MinionProjectile.fire):	# if firing
			p = Classes.MinionProjectile(minion.rect.x, minion.rect.y, True, "minions/banana.png")	#fire a banana
			direction()
		else:
			p = Classes.MinionProjectile(minion.rect.x, minion.rect.y, False, "minions/banana.png")	# fire flipped banana
			direction()

	spawn(FPS, total_frames)	# callas the spawn function
	collisions()				# calls the collition function
	#PROCESSING

##############################################################################################
def spawn(FPS, total_frames):
##############################################################################################
	four_seconds = FPS * 4	#four seconds

	if total_frames % four_seconds == 0:	# at every four seconds

		r = random.randint(1,2)	# randomize numbers 1 and 2
		x = 1 	
		if r == 2:	# if number is 2
			x = 640 - 166 	# x position

		Classes.EvilMinion(x, 20, "minions/evilminion.png")	#outputs minion at given position

##############################################################################################
def collisions():
##############################################################################################

	for enemy in Classes.EvilMinion.List:	# Loop through the evil minio list

		projectiles = pygame.sprite.spritecollide(enemy, Classes.MinionProjectile.List, True)	# initializes projectile

		for projectile in projectiles:	# Loop through the projectiles

			enemy.health = 0	# health is zero

			if projectile.if_fire:	#if fire
				enemy.image = pygame.image.load("minions/minionPoint.png")
			else:
				if enemy.velx > 0:
					enemy.image = pygame.image.load("minions/minionPoint.png")
				elif enemy.velx < 0:
					enemy.image = pygame.image.load("minions/minionPoint.png")
					#enemy.image = pygame.transform.flip(enemy.image, True, False)
			projectile.rect.x = 2 * -projectile.rect.width
			projectile.destroy()