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


	def check_edges(self):
		"""Return True if alien is at edge of screem."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:		# if right attribute of alien is greater than or equal to the right attribute of the screen
			return True

	def update(self):
		"""Move the alien left or right."""
		self.x += (self.settings.alien_speed *					# if fleet_dir is 1, value of speed will be added (moving it right); if -1 opposite
						self.settings.fleet_direction)						# takes the speed adds it to the x coordinate, then updates the alien sprites to that coordinate
		self.rect.x = self.x