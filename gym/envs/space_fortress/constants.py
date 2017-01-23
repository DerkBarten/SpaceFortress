from enum import Enum
import os

class KeyMap(Enum):
	LEFT=65361
	UP=65362
	RIGHT=65363
	SHOOT=32
	
class Games(Enum):
	SFS="SFS"
	SF="SF"
	SFC="SFC"
	AIM="AIM"

class RenderMode(Enum):
	HUMAN="human"
	MINIMAL="minimal"
	RGB_ARRAY="rgb_array"
   
class RenderSpeed(Enum):
	DEBUG=0
	SLOW=8
	MEDIUM=20
	FAST=42
	
# GAME SETTINGS FOR RUN.PY
GAME=Games.SFC
RENDER_MODE=RenderMode.HUMAN
RENDER_SPEED=RenderSpeed.DEBUG
LIBRARY_NAME="_frame_lib"
LIBRARY_PATH=str(os.path.dirname(os.path.realpath(__file__))) + "/shared"
GAME_VERSION='v0'

# OVERALL SETTINGS
DEFAULT_RENDER_MODE=RenderMode.RGB_ARRAY.value
DEFAULT_MAXSTEPS=250000
DEFAULT_TIMES=5
RECORD=False
STATS=False


print KeyMap.LEFT.value