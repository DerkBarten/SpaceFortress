from enum import Enum

class RenderMode(Enum):
	HUMAN="human"
	TERMINAL="terminal"
	MINIMAL="minimal"
	RGB_ARRAY="rgb_array"
   
class RenderSpeed(Enum):
	SLOW="slow"
	FAST="fast"


	
class Settings:
	DEFAULT_RENDER_MODE=RenderMode.HUMAN.value
	DEFAULT_RENDER_SPEED=RenderSpeed.FAST.value
	DEFAULT_DEBUG=False
	
	def __init__(self):
		self.render_speed = Settings.DEFAULT_RENDER_SPEED
		self.render_mode = Settings.DEFAULT_RENDER_MODE
		self.debug = Settings.DEFAULT_DEBUG