import pygame.font

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, ai_game):
		"""Initialize scorekeeping attributes."""
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

	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = round(self.stats.score, -1)				# Round the stats.score to the nearest 10 and store inm rounded_score
		score_str = "{:,}".format(rounded_score)				# A string formatting directive inserts commas into numbers when converting a numerical value to a string
		self.score_image = self.font.render(score_str, True,	# ...then we pass this string to render() which creates the image (including bg color and text color)
				self.text_color, self.bg_color)					# (the TRUE value is a boolean for antialiasing)

		#Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()			# Creating rect location to position score to upperight corner of the screen 
		self.score_rect.right = self.screen_rect.right - 20		# We set its right edge 20 pixels from the right edge of the screen
		self.score_rect.top = 20								# We then place the top edge 20 pixels down from the top of screen

	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
				self.text_color, self.bg_color)

		# Display the Highscore at the top center of screen.
		self.high_score_rect = self.high_score_image.get_rect()		# Creating rect location to position highscore to upper center of the screen 
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top


	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_image, self.score_rect)				# Method draws the score image onscreen at the location score_rect specifies.
		self.screen.blit(self.high_score_image, self.high_score_rect)	# Same^^ but for highscore

	def check_high_score(self):
		"""Check to see if there's a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()						# if high score, updates high_score and calls prep_high_score() to update high score image.