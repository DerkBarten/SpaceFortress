#!/usr/bin/env python
import gym
import sys
import numpy as np
from random import random
import cv2 # remove at one point
from time import sleep
from pynput.keyboard import KeyCode, Key, Listener
from constants import *

# Specify the game the gym environment will play.
# All games are registered in gym/envs/__init__.py
# All possible versions of space fortress are located in constants.py
game_name = GAME.value + "-" + GAME_VERSION
env = gym.make(game_name)

# Configure enviroment

# Get the length of the scripts
if GAME.value == "SFC":
    script_length = len(ScriptsSFC.SCRIPT1.value) 
elif GAME.value == "SF" or GAME.value == "SFS":
    script_length = len(ScriptsSF.SCRIPT1.value)
elif GAME.value == AIM:
    script_length = 1 # to be implemented
    
env.configure(mode=RENDER_MODE, record_path=None, no_direction=False, frame_skip=script_length)


def on_press(key):
    key = str(key).replace("'", "")  # Get keyboard input
    global current_key               # Global var to use outside function
    
    # Keymap input to action space using dictionary
    if GAME.value == "SF" or GAME.value == "SFS":
        key_to_action = {"uz" : 0, "ux" : 1, "uc" : 2, "uv" : 3, "ub" : 4} 
        
    elif GAME.value == "SFC":
        key_to_action = {"uz" : 0, "ux" : 1, "uc" : 2, "uv" : 3, "ub" : 4, "un" : 5, "um" : 6} 
        
    elif GAME.value == "AIM":
        key_to_action = {"uz" : 0, "ux" : 1, "uc" : 2} 
        
    if key in key_to_action.keys():
        current_key = key_to_action[key]

# Do nothing on release 
def on_release(key):
    pass

# Current key has to be initialized before first input of keyboard
current_key = 0

def play(times=DEFAULT_TIMES, max_steps=DEFAULT_MAXSTEPS):
    # Start listening to the keyboard
    with Listener(on_press=on_press, on_release=on_release) as listener:
        # Stop listening if sample actions should be used instead of keyboard
        if RENDER_SPEED != RenderSpeed.DEBUG:
            listener.stop()
            
	for game in range(times):
		env.reset()
		for t in range(max_steps):
			env.render(mode=RENDER_MODE.value)
			if RENDER_SPEED == RenderSpeed.DEBUG:
                            action = current_key
			else:
                            action = env.action_space.sample()
			observation, reward, done, _ = env.step(action)
	if WRITE_STATS:
		env.write_out_stats("test")
		env.close()
	
play()