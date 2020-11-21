import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, ai_game):
		"""Initialize the alien and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings			# we create a settings parameter so we can access the alien's speed from settings in update()

		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width							# Initially we place each alien near top left cornor; we all a space to the..
		self.rect.y = self.rect.height							# left of it that's equal to the alien's width and a space above it equal to its height

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)								# mainly concerned w/  aliens x speed, so we track x speed precisely

	def update(self):
		"""Move the alien to the right."""
		self.x += self.settings.alien_speed						# takes the speed adds it to the x coordinate, then updates the alien sprites to that coordinate
		self.rect.x = self.x