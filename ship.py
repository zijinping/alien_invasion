import pygame

class Ship():
	def __init__(self,ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings
		#load image
		self.image = pygame.image.load('images/ship2.bmp')
		self.rect =self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False

	def update(self):
		self.centerx = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
		if self.move_right and self.rect.centerx < (self.ai_settings.screen_width-10):
			self.centerx += self.ai_settings.ship_speed
		if self.move_left and self.rect.centerx >10:
			self.centerx -= self.ai_settings.ship_speed
		if self.move_up and self.rect.bottom > 40:
			self.bottom -= self.ai_settings.ship_speed
		if self.move_down and self.rect.bottom < self.ai_settings.screen_height:
			self.bottom += self.ai_settings.ship_speed
		self.rect.centerx = self.centerx
		self.rect.bottom = self.bottom

	def center_ship(self):
		self.rect.centerx = self.screen_rect.centerx
		self.rect.left = 0

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
