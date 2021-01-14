import pygame
from pygame import mixer

class Sounds:
	"""A class to store all music settings for Alien Invasion"""

	def __init__(self, ai_game):
		"""Initialize the game's music settings."""
		# Background music
		pygame.mixer.init()

	def play_bg_music(self):
		"""Play game music when game starts"""
		mixer.music.load('sound/synth.mp3')
		mixer.music.set_volume(0.5)
		mixer.music.play(-1)

	def play_bullet_sound(self):
		"""Sound created when bullet fired"""
		bullet_sound = mixer.Sound('sound/laser4.mp3')
		bullet_sound.play()

	def play_collision_sound(self):
		"""Sound created with bullet collision"""
		collision_sound = mixer.Sound('sound/boom6.wav')
		collision_sound.set_volume(1.0)
		collision_sound.play()