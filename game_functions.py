import sys
import pygame
from bullet import Bullet
from alien import Alien
from pygame.sprite import Sprite
from time import sleep
import json

def initiate_game(ai_settings,aliens,bullets,screen,ship,stats):
	ai_settings.reset_settings
	ship.center_ship()
	aliens.empty()
	bullets.empty()
	create_fleet(ai_settings,aliens,screen)
		
def check_keydown_event(ai_settings,aliens,bullets,event,screen,ship,stats):
	if event.key == pygame.K_q:
		if stats.game_score > stats.high_score:
			with open('Game_Record.json','w') as f_obj:
				json.dump(stats.game_score,f_obj)
			
		sys.exit()
	elif event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left = True
	elif event.key == pygame.K_UP:
		ship.move_up = True
	elif event.key == pygame.K_DOWN:
		ship.move_down = True
	elif event.key == pygame.K_SPACE:
		#work only when game stats is active
		if stats.game_active is True:
			if len(bullets)<ai_settings.bullet_allowed:
				new_bullet = Bullet(ai_settings,screen,ship)
				bullets.add(new_bullet)

def check_keyup_event(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	elif event.key == pygame.K_LEFT:
		ship.move_left = False
	elif event.key == pygame.K_UP:
		ship.move_up = False
	elif event.key == pygame.K_DOWN:
		ship.move_down = False

def check_events(ai_settings,aliens,bullets,play_button,screen,ship,stats):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_event(ai_settings,aliens,bullets,event,screen,ship,stats)
			elif event.type == pygame.KEYUP:
				check_keyup_event(event,ship)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y =pygame.mouse.get_pos()
				mouse_play_event(ai_settings,aliens,bullets,mouse_x,mouse_y,play_button,screen,ship,stats)
				
def mouse_play_event(ai_settings,aliens,bullets,mouse_x,mouse_y,play_button,screen,ship,stats):
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		pygame.mouse.set_visible(False)
		stats.game_active = True
		stats.reset_stats()
		initiate_game(ai_settings,aliens,bullets,screen,ship,stats)

def update_bullet(ai_settings,bullets):
	for bullet in bullets.copy():
		if bullet.rect.x > ai_settings.screen_width:
			bullets.remove(bullet)
	for bullet in bullets:
		bullet.update(ai_settings)
		bullet.draw_bullet()

def get_number_aliens_y(ai_settings,screen):
	alien = Alien(ai_settings,screen)
	#available space is the height deduct height of two aliens
	available_space_y = ai_settings.screen_height-alien.rect.height*2
	number_aliens_y = available_space_y/(2*alien.rect.height)
	return number_aliens_y

def create_alien(ai_settings,aliens,i,j,screen):
	new_alien = Alien(ai_settings,screen)
	new_alien.rect.y=(i+1)*new_alien.rect.height*2
	new_alien.rect.x = ai_settings.screen_width - 2*(j+1)*new_alien.rect.width
	aliens.add(new_alien)

def create_fleet(ai_settings,aliens,screen):
	#To calculate how many aliens can be accommodated in one row
	number_aliens_y = get_number_aliens_y(ai_settings,screen)
	#Draw 4 rows aliens
	for j in range (4):
		for i in range(int(number_aliens_y)):
			create_alien(ai_settings,aliens,i,j,screen)

def aliens_update(ai_settings,aliens,bullets,screen,ship,stats):
	#update first
	for alien in aliens:
		alien_y = float(alien.rect.y)
		alien_y += ai_settings.alien_speed
		alien.rect.y = alien_y
			
	group_bottom = 0
	group_top = ai_settings.screen_height
	group_left = ai_settings.screen_width
	for alien in aliens:
		if alien.rect.top < group_top:
			group_top = alien.rect.top
		if alien.rect.bottom>group_bottom:
			group_bottom = alien.rect.bottom
		if alien.rect.left<group_left:
			group_left = alien.rect.left
				
	if group_left <=0:
		game_accident(ai_settings,aliens,bullets,screen,ship,stats)
	elif group_bottom >= ai_settings.screen_height or group_top <= 0:
		#change the dirction of alien's movement
		ai_settings.alien_speed = -1*ai_settings.alien_speed
		for alien in aliens:
			alien.rect.x -= alien.rect.width
	

def bullets_update(ai_settings,aliens,bullets,screen,stats):
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	#add the game_score
	if collisions:
		for aliens in collisions.values():
			for alien in aliens:
				stats.stats_update()
	if len(aliens)==0:
		bullets.empty()
		create_fleet(ai_settings,aliens,screen)
		ai_settings.level_up()
		stats.level += 1

def aliens_ship_update(ai_settings,aliens,bullets,screen,ship,stats):
	if pygame.sprite.spritecollideany(ship,aliens):
		game_accident(ai_settings,aliens,bullets,screen,ship,stats)
		
def game_accident(ai_settings,aliens,bullets,screen,ship,stats):
	print("Ship hit!!!")
	sleep(0.5)
	stats.ship_left -= 1
	if stats.ship_left >0:
		initiate_game(ai_settings,aliens,bullets,screen,ship,stats)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
		print("Game over!")

def update_screen(ai_settings,aliens,bullets,play_button,score_button,screen,ship,stats):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	update_bullet(ai_settings,bullets)
	aliens.draw(screen)
	score_button.update(stats)
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()
