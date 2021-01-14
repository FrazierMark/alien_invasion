import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" A class to manage bullets fired from the ship"""

	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# Create a bullet rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,			# Create bullet's rect attribute. (Isnt based on image so we have to build a rect from scratch
			self.settings.bullet_height)									# using the pygame.Rect() class which requires x&y coordinates of topleft cornor and width and height of the rect.
		self.rect.midtop = ai_game.ship.rect.midtop							# we set the bullet's midtop attribute to match the ship's midtop attribute

		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)

		self.shoot_delay = 250
		self.last_shot = pygame.time.get_ticks()

	def update(self):
		"""Move the bullet up the screen."""							# Manages the bullet's position. When bullet fired, it moves up the screen, which corresponds
		# Update the decimal position of the bullet.					# to a decreasing y-coordinate value. To update the position, we subtract the amount stored in
		self.y -= self.settings.bullet_speed							# settings.bullet_speed from self.y
		# Update the rect position.
		self.rect.y = self.y 											# We use the value of self.y to set the value of self.rect.y (gets position of rect on every
																		# loop to later be redrawn)
	def draw_bullet(self):
		"""Draw the bullet to the screen."""							# To draw the bullet we call draw_bullet(). The draw.rect() functions fills the part of the screen
		pygame.draw.rect(self.screen, self.color, self.rect)			# defined by the bullet's rect with the color stored in self.color
