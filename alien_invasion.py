import sys

import pygame

def run_game():
	#initiate the game
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")

	#set the screen color
	bg_color = (230,230,230)

	#start the main loop of the game
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#fill the screen
		screen.fill(bg_color)	

		#Display the screen
		pygame.display.flip()

run_game()
