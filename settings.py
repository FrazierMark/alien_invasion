import pygame

class Settings:
	"""A class to store all settigs for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Bullet settings
		self.bullet_speed = 3.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 0, 60)
		self.bullets_allowed = 3

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_image = pygame.image.load('images/background.jpg')

		# Ship Settings
		self.ship_speed = 4.0

		# Alien settings
		self.alien_speed = 1.0