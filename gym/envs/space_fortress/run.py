# -*- coding: utf-8 -*-

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

global current_key
def on_press(key):
	#		LEFT = 0
	#		UP = 1
	#		RIGHT = 2
	#		SHOOT = 3
	global current_key

	key_to_action = {Key.left : 0, Key.up : 1, Key.right : 2, Key.space : 3, Key.down : 3}

	if key in key_to_action.keys():
		current_key = key_to_action[key]
	else:
		current_key = 4


def on_release(key):
	return


parser = argparse.ArgumentParser()
arg = parser.add_argument_group('Rendering')
arg.add_argument("--mode", choices=[RenderMode.HUMAN.value, RenderMode.MINIMAL.value, RenderMode.TERMINAL.value, RenderMode.RGB_ARRAY.value], 
		  default=RenderMode.HUMAN.value, help="Render Modes")
arg.add_argument("--speed", choices=[RenderSpeed.SLOW.value, RenderSpeed.FAST.value], default=RenderSpeed.FAST.value, help="Determine the render speed of the game")
args = parser.parse_args()

settings = Settings()
settings.render_mode=args.mode
settings.render_speed=args.speed
env = gym.make('SFS-v0')

# Configure enviroment
#-------------------------------
env.giveSettings(settings)
env.configure(mode=settings.render_mode, record_path=None, no_direction=False, frame_skip=1)

#with Listener(on_press=on_press, on_release=on_release) as listener:
		

def play(times=5, max_steps=250000):
	for game in range(times):
		env.reset()
		for t in range(max_steps):
			env.render()
			if settings.debug == True:
				action = current_key
			else:
				action = env.action_space.sample()


			# Uncomment this for perfect play 👌
	#           ==============================
	#			if 0.7 < random():
	#				action = env.best_action()
	#			else:
	#				env.best_waction()
	#			==============================

			observation, reward, done, _ = env.step(action)
			print(reward)

			if done:
				print("terminal")
				break
	#			print("Done!")
	#			count += 1
				# print("Episode finished after {} timesteps".format(t+1))
	#				break

#	env.write_out_stats("test")
#	env.close()
	
play()