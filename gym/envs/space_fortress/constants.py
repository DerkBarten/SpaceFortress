from enum import Enum
import os

# Key bindings: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html
# Look at '.keysym_num'
class KeyMap(Enum):
	LEFT=65361
	UP=65362
	RIGHT=65363
	SHOOT=32
	
class ScriptsSF(Enum):
        # Sample scripts for now
        # Script 1: Move left 2 times then shoot
        SCRIPT1=[KeyMap.LEFT.value,KeyMap.LEFT.value,KeyMap.SHOOT.value]
        # Script 2: Move right 2 times then shoot
        SCRIPT2=[KeyMap.RIGHT.value,KeyMap.RIGHT.value,KeyMap.SHOOT.value]
        # Script 3: Move forward 3 times
        SCRIPT3=[KeyMap.UP.value,KeyMap.UP.value,KeyMap.UP.value]
        # Script 4: Move left then forward twice
        SCRIPT4=[KeyMap.LEFT.value,KeyMap.UP.value,KeyMap.UP.value]
        # Script 5: Move Right then forward twice
        SCRIPT5=[KeyMap.RIGHT.value,KeyMap.UP.value,KeyMap.UP.value]
        
class ScriptsSFC(Enum):
        # Sample scripts for now
        # Script 1: Move left 2 times then right
        SCRIPT1=[KeyMap.LEFT.value,KeyMap.LEFT.value,KeyMap.RIGHT.value]
        # Script 2: Move right 2 times then left
        SCRIPT2=[KeyMap.RIGHT.value,KeyMap.value.RIGHT.value,KeyMap.LEFT.value]
        # Script 3: Move right 3 times
        SCRIPT3=[KeyMap.RIGHT.value,KeyMap.RIGHT.value,KeyMap.RIGHT.value]
        # Script 4: Move left then forward twice
        SCRIPT4=[KeyMap.LEFT.value,KeyMap.UP.value,KeyMap.UP.value]
        # Script 5: Move Right then forward twice
        SCRIPT5=[KeyMap.RIGHT.value,KeyMap.UP.value,KeyMap.UP.value]
	
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
	# actually more of a render delay than speed
	DEBUG=0
	SLOW=42
	MEDIUM=20
	FAST=8
	
# GAME SETTINGS FOR RUN.PY
GAME=Games.SFC
RENDER_MODE=RenderMode.HUMAN
RENDER_SPEED=RenderSpeed.FAST
LIBRARY_NAME="_frame_lib"
LIBRARY_PATH=str(os.path.dirname(os.path.realpath(__file__))) + "/shared"
GAME_VERSION='v0'

# OVERALL SETTINGS
DEFAULT_RENDER_MODE=RenderMode.RGB_ARRAY.value
DEFAULT_MAXSTEPS=250000
DEFAULT_TIMES=5
RECORD=False
STATS=False
