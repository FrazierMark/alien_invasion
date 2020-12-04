import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
	"""A class to manage explosions from bullet/alien collisions."""

	def __init__(self, ai_game):
		"""Create an explosion animation at the alien's current position"""
		super().__init__()
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.explosion_animation = {}
		self.explosion_animation['lg'] = []

		self.prep_explosion()


	def prep_explosion(self):
		"""Load explosion from PNGs"""
		for i in range(9):
			self.filename = 'regularExplosion0{}.png'.format(i)
			self.explosion_img = pygame.image.load('images/filename')
			self.explosion_img.set_colorkey(BLACK)
			self.explosion_animation['lg'].append(explosion_img)
