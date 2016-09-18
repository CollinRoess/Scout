'''
Scout: A 2D back-and-forth button masher written for my daughter.
Written by Collin Roess
9/5/2016

'''


import pygame, random

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
purple = (175,0,175)

dogImg = pygame.image.load('dogimage.png')
revdog = pygame.image.load('dogimageright.png')
dogimg_width = 110


def game_loop():	
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0

	pygame.init()
	gameDisplay = pygame.display.set_mode((display_width, display_height))
	pygame.display.set_caption('')
	clock = pygame.time.Clock()
	rev=False
	def dog(x, y):
		if rev==False:
			gameDisplay.blit(dogImg, (x, y))
		else:
			gameDisplay.blit(revdog, (x,y))
	def reset():
		x = (display_width * 0.45)
		y = (display_height * 0.8)
	
	crashed = False

	while not crashed:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed =  True
		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					rev=False
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					rev=True
					x_change = 5
				else:
					rev=random.choice([True,False])
					if rev==True:
						x_change = 5
					else:
						x_change = -5
					
			if event.type == pygame.KEYUP:
				x_change=0
					
			
            
		x += x_change
		
		if x > display_width -dogimg_width:
			rev = False
			x_change = -5
		if x<=0:
			rev = True
			x_change = 5

			
		gameDisplay.fill(purple)	
		dog(x,y)	
		pygame.display.update()
		clock.tick(60)
		

	
game_loop()
pygame.quit()
quit()