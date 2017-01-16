from enum import Enum

class Games(Enum):
	SFS="SFS"
	SF="SF"
	SFC="SFC"
	AIM="AIM"

GAME_VERSION='v0'

class RenderMode(Enum):
	HUMAN="human"
	TERMINAL="terminal"
	MINIMAL="minimal"
	RGB_ARRAY="rgb_array"
   
class RenderSpeed(Enum):
	SLOW_NAME="slow"
	FAST_NAME="fast"
	SLOW_VALUE=43
	FAST_VALUE=10

DEFAULT_MAXSTEPS=250000
DEFAULT_TIMES=5
DEFAULT_GAME=Games.SFS.value
LIBRARY_NAME="_frame_lib"
WRITE_STATS=False
	
class Settings:
	DEFAULT_RENDER_MODE=RenderMode.HUMAN.value
	DEFAULT_RENDER_SPEED=RenderSpeed.FAST_NAME.value
	DEFAULT_DEBUG=False
	
	
	
	def __init__(self):
		self.render_speed = Settings.DEFAULT_RENDER_SPEED
		self.render_mode = Settings.DEFAULT_RENDER_MODE
		self.debug = Settings.DEFAULT_DEBUG