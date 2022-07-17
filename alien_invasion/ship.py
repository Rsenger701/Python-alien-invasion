#Richard Senger 2/10/22

#Ship

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen #we assign the screen to an attribute of ship.
		self.screen_rect = ai_game.screen.get_rect() # We access the screen's rect attribute by get_rect().
		self.settings = ai_game.settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp') #This will load the image and give it the location of the image.
		self.rect = self.image.get_rect()
		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom # This will choose the ships position.
		# Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)

		# Movement flags
		self.moving_right = False #adding self moving right attribute.
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		#update ship's x value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed # This will result in ship standing still if both keys are pressed.
		# Update rect object from self.x.
		self.rect.x = self.x


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect) #this draws the image at the position specified by self.rect.

	def center_ship(self):
		"""Center the ship on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)