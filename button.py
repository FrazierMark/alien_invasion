import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		"""Initialie button attributes."""
		self.screen = ai_game.screen 					# We assign the game screen to the attribute of the Button, so we can access it easily
		self.screen_rect = self.screen.get_rect()		# We access the screen's rect attribute using the get_rect() method and assign to self.screen_rect

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)		# We prepare a font attribute. None is default font, 48 is the sixe of text

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)	# We create a rect for the button... 
		self.rect.center = self.screen_rect.center				#... and set its center attribute to match that of the screen

		# The button message needs to be prepped oly once.
		self._prep_msg(msg)