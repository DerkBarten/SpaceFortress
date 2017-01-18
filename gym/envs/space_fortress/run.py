#!/usr/bin/env python
import gym
import sys
import numpy as np
from random import random
import cv2 # remove at one point
from time import sleep
from pynput.keyboard import Key, Listener
from constants import *

game_name = GAME.value + "-" + GAME_VERSION
env = gym.make(game_name)

# Configure enviroment
env.configure(mode=RENDER_MODE, record_path=None, no_direction=False, frame_skip=1)
		
def play(times=DEFAULT_TIMES, max_steps=DEFAULT_MAXSTEPS):
	for game in range(times):
		env.reset()
		for t in range(max_steps):
			env.render(mode=RENDER_MODE.value)
			if RENDER_MODE== RenderSpeed.DEBUG:
				action = current_key
			else:
				action = env.action_space.sample()
			observation, reward, done, _ = env.step(action)
	if WRITE_STATS:
		env.write_out_stats("test")
		env.close()
	
play()