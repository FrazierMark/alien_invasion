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

		# Prepare the initial score image.
		self.prep_score()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		score_str = str(self.stats.score)						# We convert stats.score into string...
		self.score_image = self.font.render(score_str, True,	# ...then we pass this string to render() which creates the image (including bg color and text color)
				self.text_color, self.bg_color)					# (the TRUE value is a boolean for antialiasing)

		#Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()			# Creating rect location to position score to upperight corner of the screen 
		self.score_rect.right = self.screen_rect.right - 20		# We set its right edge 20 pixels from the right edge of the screen
		self.score_rect.top = 20								# We then place the top edge 20 pixels down from the top of screen

	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_image, self.score_rect)		# Method draws the score image onscreen at the location score_rect specifies.