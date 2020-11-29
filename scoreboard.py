import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, ai_game):
		"""Initialize scorekeeping attributes."""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Font settings for scoring information.
		self.text_color = (255, 0, 0)
		self.bg_color = (110, 0, 110)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = round(self.stats.score, -1)				# Round the stats.score to the nearest 10 and store inm rounded_score
		score_str = "{:,}".format(rounded_score)				# A string formatting directive inserts commas into numbers when converting a numerical value to a string
		label_score = f"Score: {score_str}"
		self.score_image = self.font.render(label_score, True,	# ...then we pass this string to render() which creates the image (including bg color and text color)
				self.text_color, self.bg_color)					# (the TRUE value is a boolean for antialiasing--smoother text edges)

		#Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()			# Creating rect location to position score to upperight corner of the screen 
		self.score_rect.right = self.screen_rect.right - 20		# We set its right edge 20 pixels from the right edge of the screen
		self.score_rect.top = 20								# We then place the top edge 20 pixels down from the top of screen

	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		label_high_score = f"Highscore: {high_score_str}"
		self.high_score_image = self.font.render(label_high_score, True,
				self.text_color, self.bg_color)

		# Display the Highscore at the top center of screen.
		self.high_score_rect = self.high_score_image.get_rect()		# Creating rect location to position highscore to upper center of the screen 
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top


	def show_score(self):
		"""Draw scores, level, and ships to the screen."""
		self.screen.blit(self.score_image, self.score_rect)				# Method draws the score image onscreen at the location score_rect specifies.
		self.screen.blit(self.high_score_image, self.high_score_rect)	# Same^^ but for highscore
		self.screen.blit(self.level_image, self.level_rect)				# Same, but for Level
		self.ships.draw(self.screen)									# we call draw() on the groups and Pygame draws each ship

	def check_high_score(self):
		"""Check to see if there's a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()						# if high score, updates high_score and calls prep_high_score() to update high score image.

	def prep_level(self):
		"""Turn the level into a rendered image."""
		level_str = str(self.stats.level)						# Convert stats.level to string
		label_level_str = f"Level: {level_str}"
		self.level_image = self.font.render(label_level_str, True,
				self.text_color, self.bg_color)					# Renders text to an image

		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()			# Creating rect location to position Level to u of the screen 
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10


	def prep_ships(self):
		"""Show how many ships are left."""
		self.ships = Group()								# create an empty group, self.ships to hold the ship instances
		for ship_number in range(self.stats.ships_left):	# to fill group, loop runs once for every ship the player has left
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)							# We add each new ship to the group ships

