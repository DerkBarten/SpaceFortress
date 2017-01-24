#!/usr/bin/env python
import gym
import sys
import numpy as np
from random import random
import cv2 # remove at one point
from time import sleep
from pynput.keyboard import Key, Listener
from constants import *

# Specify the game the gym environment will play.
# All games are registered in gym/envs/__init__.py
# All possible versions of space fortress are located in constants.py
game_name = GAME.value + "-" + GAME_VERSION
env = gym.make(game_name)

# Configure enviroment
env.configure(mode=RENDER_MODE, record_path=None, no_direction=False, frame_skip=1)

#  Keymap:
#  LEFT = 0
#  UP = 1
#  RIGHT = 2
# Shooting can be implemented later
def on_press(key):
    # Global var to use outside function
    global current_key 
    
    # Keymap input to action space
    key_to_action = {Key.left : 0, Key.up : 1, Key.right : 2} 

    if key in key_to_action.keys():
        current_key = key_to_action[key]

# Do nothing on release 
def on_release(key):
    pass

# Current key has to be initialized before first input of keyboard
current_key = 1

def play(times=DEFAULT_TIMES, max_steps=DEFAULT_MAXSTEPS):
    with Listener(on_press=on_press, on_release=on_release) as listener:
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