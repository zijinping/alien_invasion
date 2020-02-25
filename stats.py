import json

class Stats():
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.game_active = False
		#when game starts again, set the score and level back.
		self.reset_stats()
		# the score system
		self.level_score_dict = {1:30,2:40,3:50,4:60,5:70,6:80,7:90,8:100,9:110,10:120}
		#load high score
		with open('Game_Record.json','w+') as f_obj:
			try:
				self.high_score = json.load(f_obj)
			except json.decoder.JSONDecodeError:
				self.high_score = 0
		
	def reset_stats(self):
		self.ship_left = self.ai_settings.ship_limit
		self.game_score = 0
		self.level = 1

	def stats_update(self):
		self.game_score += self.level_score_dict[self.level]
		
		

