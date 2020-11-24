import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and game resources."""
		pygame.init()
		self.settings = Settings()											# import Settings into the main program file

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)		# passig a wiondow size of 0,0 to FULLSCREEN tells Pygame to figure out window size to fill screen
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height			# creates  a display window, will draw the game's graphical elements
		pygame.display.set_caption("Alien Invasion")						# tuple that defines dimensions by referencing the attributes in self.settings

		# Create an instance to store game statistics.
		self.stats = GameStats(self)

		self.ship = Ship(self)										# the self arg refers to the current instance of AlienInvasion
																	# Parameter gives Ship access to the game's resources, such as screen object
		self.bullets = pygame.sprite.Group()							# We use this group to draw bullets to the screen on each pass through...
																	# ...the main loop and to update each bullet's position.
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()										# function in ship.py, updates position of ship image
				self._update_bullets()
				self._update_aliens()
				
			self._update_screen()


	def _check_events(self):										# "Helper Method" Does work inside a class but isn't meant to be called through an instance	
		"""Respond to keypresses and mouse events"""				# def run_game calls this method (easier to keep code clean and clear)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:						# Pygame responds if it detects a KEYDOWN event
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:						# else if player releases the right arrow, we set moving_right back to false
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses"""
		if event.key == pygame.K_RIGHT:								# if R arrow pressed we set moving right to True
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:							# if L arrow pressed we set moving left to True
			self.ship.moving_left = True							
		elif event.key == pygame.K_UP:								# if UP arrow pressed we set moving up to True
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:							# if DOWN arrow pressed we set moving down to True
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:							# if spacebar is pressed we call _fire_bullet()
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Respnd to key releases."""
		if event.key == pygame.K_RIGHT:								# (otherwise it would be left true and ship would continue moving R after keydown event)
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_q:								# if Q is pressed, game quits.
			sys.exit()

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:			# we check the length of bullets currently on screen, if limit not reached we...	
			new_bullet = Bullet(self)									# ...make an instancve of Bullet and call it new_bullet
			self.bullets.add(new_bullet)								# we then add it to the group BULLETS using the add() method (similar to append() for Pygame)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		# Update bullet positions.
		self.bullets.update()									# the group auto calls update() for each sprite in the group	

		# Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""Respond to bullet-alien collisions."""
		# Remove any bullets and aliens that have collided
		collisions = pygame.sprite.groupcollide(				#compares the position of all bulets in self.bullets and all the aliens in self.aliens
				self.bullets, self.aliens, True, True)			# if overlap, collide() adds a key-value pair to the dic it returns, removes bullets and aliens

		if not self.aliens:										# we check if alien group is empty
			# Destroy existing hullets and create new fleet.
			self.bullets.empty()								# if alien group empty, we remove existing bullets by using empty() method
			self._create_fleet()								# We then call _create_fleet(), which fills the screen with aliens again

	def _update_aliens(self):
		"""Chk if the fleet is at an edge,
			then update the position of all aliens in the fleet."""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for alien-ship collisions.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):	# spritecollideany() functions takes 2 args, sprite and a group.
			self._ship_hit()							# if spritecollideany() returns None, if block doesn't execute

		# Look for aliens hitting the bottom of the screen.
		self._check_aliens_bottom()


	def _check_fleet_edges(self):
		"""Respond appropriately if any aliensw have reached an edge."""
		for alien in self.aliens.sprites():					# if check_edges() returns true we know an alien is at edge and direction needs to change
			if alien.check_edges():
				self._change_fleet_direction()				# ...so we call _change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1				# after fleet has dropped, we change the value of fleet_direction by multiplying its current value by -1


	def _create_fleet(self):
		"""Create the fleet of aliens."""
		# Create an alien and find the number of aliens in a row.
		# Spacing between each alien is equal to one alien width.
		alien = Alien(self)											# we create 1 alien to get width and height
		alien_width, alien_height = alien.rect.size 				# size contains a tuple with the width and height of a rect object 
		available_space_x = self.settings.screen_width - (2 * alien_width)	# we calculate x space available for aliens and # of aliens that can fit
		number_aliens_x = available_space_x // (2 * alien_width)
		
		# Create  the number of rows of aliens that fit on screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
								(3 * alien_height) - ship_height)
		number_rows = available_space_y // (3 * alien_height)

		# Create the full fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):					# create loop that counts from 0 to # of aliens calculated above
			# Create an alien and place it in the row.
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		"""Create an alien and place it in the row."""
		alien = Alien(self)										# create alien
		alien_width, alien_height = alien.rect.size 
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x 													# We use the alien's x attribute to se the position of its rect
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)													# we create an alien, then add that alien to the alien sprite Group() that will hold the fleet


	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""		# Redraw the screen during each pass through the loop.
		# re-scale background image
		self.scaled_bg_image = pygame.transform.scale(self.settings.bg_image, (self.screen.get_rect().width, self.screen.get_rect().height))
		# draw re-scaled image to screen using blit() method
		self.screen.blit(self.scaled_bg_image, [0, 0])

		self.ship.blitme()												# we draw the ship on the screen by calling ship.blitme()
		for bullet in self.bullets.sprites():					# .sprites() method returns a list of all sprites in the group bullets
			bullet.draw_bullet()								# to draw all fired bullets, we loop though the sprites in bullets and call draw_bullet on each
		# draws each element in group at the position defined by its rect attribute
		self.aliens.draw(self.screen)							# the draw() method requires one arg: a surface on which to draw
		
		pygame.display.flip()									# Make the most recently drawn screen visible.

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien"""
		if self.stats.ships_left > 0:
			# Decrement ships_left
			self.stats.ships_left -= 1 

			# Get rid of any remaining aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()

			# Pause.
			sleep(0.5)
		else:
			self.stats.game_active = False

	def _check_aliens_bottom(self):
		"""Check if any aliens have reached the bottom of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Treat this the same as if the ship got hit.
				self._ship_hit()
				break


if __name__ == '__main__':
	# Make a game instance, and run the gmae.
	ai = AlienInvasion()
	ai.run_game()									# Set the background color by accessing the attributes in settings.