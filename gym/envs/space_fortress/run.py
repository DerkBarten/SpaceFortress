#!/usr/bin/env python
import gym
import sys
import numpy as np
from random import random
import cv2 # remove at one point
from time import sleep
from pynput.keyboard import Key, Listener
import argparse
from settings import *

# the commandline options
parser = argparse.ArgumentParser()
garg = parser.add_argument_group('Game')
garg.add_argument("-g", choices=[Games.SFS.value, Games.SF.value, Games.SFC.value, Games.AIM.value], 
		  default=Games.SFS.value, help="Specify which game you want to run")
rarg = parser.add_argument_group('Rendering')
rarg.add_argument("-m", choices=[RenderMode.HUMAN.value, RenderMode.MINIMAL.value, RenderMode.TERMINAL.value, RenderMode.RGB_ARRAY.value], 
		  default=RenderMode.HUMAN.value, help="Determine the render mode of the game")
rarg.add_argument("-s", choices=[RenderSpeed.SLOW_NAME.value, RenderSpeed.FAST_NAME.value], 
		  default=RenderSpeed.FAST_NAME.value, help="Determine the render speed of the game")
rargs = parser.parse_args()
gargs = parser.parse_args()

settings = Settings()
settings.render_mode=rargs.m
settings.render_speed=rargs.s

game_name = gargs.g + "-" + GAME_VERSION
env = gym.make(game_name)

# Configure enviroment
#-------------------------------
env.giveSettings(settings)
env.configure(mode=settings.render_mode, record_path=None, no_direction=False, frame_skip=1)
		

def play(times=DEFAULT_TIMES, max_steps=DEFAULT_MAXSTEPS):
	for game in range(times):
		env.reset()
		for t in range(max_steps):
			env.render()
			if settings.debug == True:
				action = current_key
			else:
				action = env.action_space.sample()
			observation, reward, done, _ = env.step(action)
			if done:
				print("terminal")
				break
	if WRITE_STATS:
		env.write_out_stats("test")
		env.close()
	
play()