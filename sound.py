import pygame
from pygame import mixer

class Sound:
	"""A class to store all music settings for Alien Invasion"""

	def __init__(self, ai_game):
		"""Initialize the game's music settings."""
		# Background music
		

	def play_bg_music(self):
		"""Play game music when game starts"""
		pygame.mixer.init()
		mixer.music.load('sound/synth.mp3')
		mixer.music.play(-1)