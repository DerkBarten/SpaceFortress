from enum import Enum
import os

# Key bindings: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html
# Look at '.keysym_num'
class KeyMap(Enum):
	LEFT=65361
	UP=65362
	RIGHT=65363
	SHOOT=32

# Global variables to make syntax easier
UP = KeyMap.UP.value
LEFT = KeyMap.LEFT.value
RIGHT = KeyMap.RIGHT.value
SHOOT = KeyMap.SHOOT.value

# Scripts of length 3
class ScriptsSF_3(Enum):
        # Sample scripts for now
        # Script 1: Move left 2 times then shoot
        SCRIPT1=[LEFT,LEFT,SHOOT]
        # Script 2: Move right 2 times then shoot
        SCRIPT2=[RIGHT,RIGHT,SHOOT]
        # Script 3: Move forward 3 times
        SCRIPT3=[UP,UP,UP]
        # Script 4: Move left then forward twice
        SCRIPT4=[LEFT,UP,UP]
        # Script 5: Move Right then forward twice
        SCRIPT5=[RIGHT,UP,UP]

# SCripts of length 9
class ScriptsSF_9(Enum):
	# Sample scripts for now
	# Script 1: Move left 2 times then shoot
	SCRIPT1=[LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,SHOOT,SHOOT,SHOOT]
	# Script 2: Move right 2 times then shoot
	SCRIPT2=[RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,SHOOT,SHOOT,SHOOT]
	# Script 3: Move forward 3 times
	SCRIPT3=[UP,UP,UP,UP,UP,UP,UP,UP,UP]
	# Script 4: Move left then forward twice
	SCRIPT4=[LEFT,LEFT,LEFT,UP,UP,UP,UP,UP,UP]
	# Script 5: Move Right then forward twice
	SCRIPT5=[RIGHT,RIGHT,RIGHT,UP,UP,UP,UP,UP,UP]

class ScriptsSFC_3(Enum):
        # Script 1: Move left 2 times then forward
        SCRIPT1=[LEFT,LEFT,UP]
        # Script 2: Move right 2 times then forward
        SCRIPT2=[RIGHT,RIGHT,UP]
        # Script 3: Move right 3 times
        SCRIPT3=[RIGHT,RIGHT,RIGHT]
        # Script 4: Move left 3 times
        SCRIPT4=[LEFT,LEFT,LEFT]
        # Script 5: Move forward then left twice
        SCRIPT5=[UP,LEFT,LEFT]
        # Script 6: Move forward then right twice
        SCRIPT6=[UP,RIGHT,RIGHT]
        # Script 7: Move forward thrice
        SCRIPT7=[UP,UP,UP]

class ScriptsSFC_9(Enum):
        # Script 1: Move left 2 times then forward
        SCRIPT1=[LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,UP,UP,UP]
        # Script 2: Move right 2 times then forward
        SCRIPT2=[RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,UP,UP,UP]
        # Script 3: Move right 3 times
        SCRIPT3=[RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT]
        # Script 4: Move left 3 times
        SCRIPT4=[LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,LEFT]
        # Script 5: Move forward then left twice
        SCRIPT5=[UP,UP,UP,LEFT,LEFT,LEFT,LEFT,LEFT,LEFT]
        # Script 6: Move forward then right twice
        SCRIPT6=[UP,UP,UP,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT]
        # Script 7: Move forward thrice
        SCRIPT7=[UP,UP,UP,UP,UP,UP,UP,UP,UP]

class ScriptsAIM_3(Enum):
        # Script 1: Move left 2 times then shoot
        SCRIPT1=[LEFT,LEFT,SHOOT]
        # Script 2: Move right 2 times then shoot
        SCRIPT2=[RIGHT,RIGHT,SHOOT]
        # Script 3: Move right 3 times
        SCRIPT3=[RIGHT,RIGHT,RIGHT]
        # Script 4: Move left 3 times
        SCRIPT4=[LEFT,LEFT,LEFT]
        # Script 5: Move left then shoot twice
        SCRIPT5=[LEFT,SHOOT,SHOOT]
        # Script 6: Move right then shoot twice
        SCRIPT6=[RIGHT,SHOOT,SHOOT]
        # Script 7: Shoot thrice
        SCRIPT7=[SHOOT,SHOOT,SHOOT]

class ScriptsAIM_9(Enum):
        # Script 1: Move left 2 times then shoot
        SCRIPT1=[LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,SHOOT,SHOOT,SHOOT]
        # Script 2: Move right 2 times then shoot
        SCRIPT2=[RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,SHOOT,SHOOT,SHOOT]
        # Script 3: Move right 3 times
        SCRIPT3=[RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT]
        # Script 4: Move left 3 times
        SCRIPT4=[LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,LEFT,LEFT]
        # Script 5: Move left then shoot twice
        SCRIPT5=[LEFT,LEFT,LEFT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT]
        # Script 6: Move right then shoot twice
        SCRIPT6=[RIGHT,RIGHT,RIGHT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT]
        # Script 7: Shoot thrice
        SCRIPT7=[SHOOT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT,SHOOT]

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

class EnableScripts(Enum):
        ON = "on"
        OFF = "off"

class ScriptLength(Enum):
	THREE = 3
	NINE = 9

# GAME SETTINGS FOR RUN.PY
GAME=Games.AIM
RENDER_MODE=RenderMode.HUMAN
RENDER_SPEED=RenderSpeed.DEBUG
LIBRARY_NAME="_frame_lib"
LIBRARY_PATH=str(os.path.dirname(os.path.realpath(__file__))) + "/shared"
GAME_VERSION='v0'

# OVERALL SETTINGS
SCRIPTS = EnableScripts.ON
SCRIPT_LENGTH = ScriptLength.NINE # Should be three if scripts is off
DEFAULT_RENDER_MODE=RenderMode.RGB_ARRAY.value
DEFAULT_MAXSTEPS=2500000
DEFAULT_TIMES=100
RECORD=False
STATS=False
