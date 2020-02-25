import pygame.font

class Button():
	def __init__(self,ai_settings,screen,msg):
		'''initialize the button features'''
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		#set the size of button and other feature
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		#create button and set it at middle position
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center= self.screen_rect.center

		#the button only need to be built once
		self.prep_msg(msg)

	def prep_msg(self,msg):
		'''render msg as image and locate it on the center of the bottom'''
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

class Game_Score():
	def __init__(self,ai_settings,screen):
		self.ai_settings = ai_settings
		self.screen = screen
		self.text_color = (0,0,0)
		self.font = pygame.font.SysFont(None,32)

	def update(self,stats):
		self.game_score=str(stats.game_score)
		self.msg_image = self.font.render(self.game_score,True,self.text_color,self.ai_settings.bg_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = (100,100)
		self.screen.blit(self.msg_image,self.msg_image_rect)

class High_Score():
	def __init__(self,ai_settings,screen):
		self.screen = screen
		self.text_color = (0,0,0)
	
		

		
		

