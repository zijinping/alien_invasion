import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien,self).__init__()
		self.ai_settings = ai_settings
		self.screen=screen
		#laod image and place on the top left corner
		self.image = pygame.image.load('images/alien2.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = ai_settings.screen_width-self.rect.width
		self.rect.y = self.rect.height

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		 
