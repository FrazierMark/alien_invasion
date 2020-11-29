import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings						# create a settings attribue for Ship so we can use it in update()
		self.screen_rect = ai_game.screen.get_rect()			# We accesss the screen's (GAME WINDOW) rect attribute using the get_rect() method and assign it to self.screen_rect
																# doing this allows us to place the ship in the correct location on the screen

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/rainbowship.png')		# function returns surface representing the ship, which we assign to self.image
		self.rect = self.image.get_rect()						# When image is loaded, we call get_rect() to access the ship surface's...
																# ...rect attribute so we can later use it to place the ship

		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom		# uses these rect attributes to position the ship image so it's centered horizontally and aligned with the bottom of the screen

		# Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)								# to keep track of ship position accurately we define a new self.x attribute that can hold decimal values (float)
		self.y = float(self.rect.y)

		#Movement flag
		self.moving_right = False								# adding moving right attribute in the __init__() method and set to false
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		# Update the ship's x value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:		# moves the ship right IF movement is TRUE AND it hasn't reached to right/left edge of screen
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed


		# Update rect object from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)					# we define blitme() method, which draws the image to the screen at the position specificed by self.rect

	def center_ship(self):
		"""Center the ship on the bottom screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)