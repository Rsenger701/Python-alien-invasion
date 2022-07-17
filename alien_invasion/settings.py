#Richard Senger, 2/10/22

#settings

class Settings: #This Creates a class for settings. This can be imported into alien invasion.
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 5
		
		# fleey_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 600 #This and the ^ adjust the total screen size for the game.
		self.bg_color = (230, 230, 230)# this adjusts the background color to what we want!

		# Bullet Settings
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15 
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#Ship settings
		self.ship_speed = 1.5 # we are adjusting ships overall speed.
		self.ship_limit = 3

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# How quickly the alien point value increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initalize settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
