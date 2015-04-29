




import pygame, sys, Classes, random
##############################################################################################
def process(bug, FPS, total_frames):	
##############################################################################################

	for event in pygame.event.get():
		if event.type == pygame.QUIT:	
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:	#pressing down on a key
			if event.key == pygame.K_e:	 	#if that key is e
				Classes.BugProjectile.fire = not Classes.BugProjectile.fire

	keys = pygame.key.get_pressed()

	if keys[pygame.K_d]: # d key
		Classes.Bug.going_right = True
		bug.image = pygame.image.load("images/bug1.png")
		bug.velx = 5
	elif keys[pygame.K_a]:
		Classes.Bug.going_right = False
		bug.image = pygame.image.load("images/bug2.png")
		bug.velx = -5
	else:
		bug.velx = 0

	if keys[pygame.K_w]:
		bug.jumping = True	

	if keys[pygame.K_SPACE]:

		def direction():
			if Classes.Bug.going_right:
				p.velx = 8
			else:
				p.image = pygame.transform.flip(p.image, True, False)
				p.velx = -8

		if(Classes.BugProjectile.fire):
			p = Classes.BugProjectile(bug.rect.x, bug.rect.y, True, "images/projectiles/fire.png")
			direction()
		else:
			p = Classes.BugProjectile(bug.rect.x, bug.rect.y, False, "images/projectiles/frost.png")
			direction()

	spawn(FPS, total_frames)
	collisions()
	#PROCESSING
def spawn(FPS, total_frames):
	four_seconds = FPS * 4

	if total_frames % four_seconds == 0:

		r = random.randint(1,2)
		x = 1
		if r == 2:
			x = 640 - 166

		Classes.Enemy(x, 20, "images/enemy.png")

def collisions():
#	for enemy in Classes.Enemy.List:
		
#		if pygame.sprite.spritecollide(enemy, Classes.BugProjectile.List, False):	#if there is a collision
			
#			if Classes.BugProjectile.fire:
#				enemy.health -= enemy.half_health
#			else:
#				enemy.velx = 0

#	for proj in Classes.BugProjectile.List:

#		if pygame.sprite.spritecollide(proj, Classes.Enemy.List, False):
#			proj.rect.x = 2 * -proj.rect.width
	#			proj.destroy()
	for enemy in Classes.Enemy.List:

		projectiles = pygame.sprite.spritecollide(enemy, Classes.BugProjectile.List, True)

		for projectile in projectiles:

			enemy.health = 0

			if projectile.if_fire:
				enemy.image = pygame.image.load("images/enemy.png")
			else:
				if enemy.velx > 0:
					enemy.image = pygame.image.load("images/enemy.png")
				elif enemy.velx < 0:
					enemy.image = pygame.image.load("images/enemy.png")
					enemy.image = pygame.transform.flip(enemy.image, True, False)
			projectile.rect.x = 2 * -projectile.rect.width
			projectile.destroy()