import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		self.rect = pygame.Rect(0,0,self.ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.y = ship.rect.centery
		self.rect.x = ship.rect.right
		self.color = ai_settings.bullet_color


	def update(self,ai_settings):
		self.x = float(self.rect.x)
		self.x += self.ai_settings.bullet_speed
		self.rect.x = self.x
	
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color,self.rect)
	
		
