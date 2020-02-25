class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 1200
		self.bg_color = (230, 230, 230)
		#set parameters for bullet
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (0,0,0)
		self.reset_settings()

	def reset_settings(self):
		self.ship_limit = 3
		self.ship_speed = 2
		self.bullet_speed = 4
		self.alien_speed = 1
		self.bullet_allowed = 5
	
	def level_up(self):
		self.ship_speed *= 1.1
		self.bullet_speed *= 1.1
		self.alien_speed *= 1.2
		self.bullet_allowed += 1

