import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from pygame.sprite import Group
from stats import Stats
from button import Button,Game_Score
import json

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	#Record game stas
	stats = Stats(ai_settings)
	
	#Build a ship
	ship = Ship(ai_settings, screen)
	#Build bullets group
	bullets = Group()
	#Build aliens group
	aliens = Group()
	gf.create_fleet(ai_settings,aliens,screen)
	#create play button
	play_button = Button(ai_settings,screen,"PLAY")
	score_button = Game_Score(ai_settings,screen)
	while True:
		gf.check_events(ai_settings,aliens,bullets,play_button,screen,ship,stats)
		if stats.game_active:
			#Check if collision happened 
			gf.bullets_update(ai_settings,aliens,bullets,screen,stats)
			gf.aliens_ship_update(ai_settings,aliens,bullets,screen,ship,stats)
			ship.update()
			gf.aliens_update(ai_settings,aliens,bullets,screen,ship,stats)

		gf.update_screen(ai_settings,aliens,bullets,play_button,score_button,screen,ship,stats)

run_game()
