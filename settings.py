import pygame

class Settings:
	"""A class to store all settigs for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Bullet settings
		self.bullet_speed = 3.0
		self.bullet_width = 3000
		self.bullet_height = 15
		self.bullet_color = (255, 0, 60)
		self.bullets_allowed = 3

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_image = pygame.image.load('images/background.jpg')

		# Ship Settings
		self.ship_speed = 4.0
		self.ship_limit = 3

		# Alien settings
		self.alien_speed = 2.0
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1