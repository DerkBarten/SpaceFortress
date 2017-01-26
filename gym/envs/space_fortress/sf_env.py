#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gym
from gym.utils import seeding
from gym import spaces
import ctypes
from time import sleep
from sys import platform
import datetime
import numpy as np
import cv2
import os
import csv
from pathlib import Path
import sys
from constants import *
import time

# SFEnv is a child of the environment template located in gym/core.py
# This instance handles the space fortress environment
class SFEnv(gym.Env):
	# - Class variables, these are needed to communicate with the template in gym/core.py
	metadata = {'render.modes': ['rgb_array', 'human', 'minimal', 'terminal'], 'configure.required' : True}

	# Initialize the environment 
	def __init__(self, game=GAME.value):
		# Specify the game name which will be shown at the top of the game window
		if game==Games.SFS.value:
			self.game_name = "Simple Space Fortress V2"
		elif game==Games.SF.value:
			self.game_name = "Space Fortress"
		elif game==Games.AIM.value:
			self.game_name = "Aiming Task"
		elif game==Games.SFC.value:
			self.game_name = "Control Task"
		else:
			print("Invalid game name")
			sys.exit(0)
		
		# The game which will be played, the possible games are
		# located in the enum Games in constants.py
		self.game = game
		# The size of the screen when playing in human mode
		self.screen_height = 448
		self.screen_width = 448
		 # The amount of (down) scaling of the screen height and width
		self.scale = 5.3
		# It is possible to specify a seed for random number generation
		self._seed()
		if game == Games.SFS.value or game == Games.SF.value:
			# All keys allowed
                        # Old action space single buttons
			#self._action_set = {0 : KeyMap.LEFT.value, 1 : KeyMap.UP.value, 2 : KeyMap.RIGHT.value, 3 : KeyMap.SHOOT.value}
			# New action space with scripts 
			self._action_set = {0 : ScriptsSF.SCRIPT1.value, 1 : ScriptsSF.SCRIPT2.value, 2 : ScriptsSF.SCRIPT3.value, 3 : ScriptsSF.SCRIPT4.value, 4 : ScriptsSF.SCRIPT5.value}
		if game == Games.AIM.value:
			# Only rotate left/right and shoot
			# Old action space single buttons
			self._action_set = {0 : KeyMap.SHOOT.value, 1 : KeyMap.LEFT.value, 2 : KeyMap.RIGHT.value}
		if game == Games.SFC.value:
			# Only rotate left/right and forward
			# Old action space single buttons
			#self._action_set = {0 : KeyMap.LEFT.value, 1 : KeyMap.RIGHT.value, 2 : KeyMap.UP.value} 
			# New action space with scripts
			self._action_set = {0 : ScriptsSFC.SCRIPT1.value, 1 : ScriptsSFC.SCRIPT2.value, 2 : ScriptsSFC.SCRIPT3.value, 3 : ScriptsSFC.SCRIPT4.value, 4 : ScriptsSFC.SCRIPT5.value}
			
		# The number of bytes to read in from the returned image pointer
		# which happens to be equal to the amount of pixels in the image
		self.n_bytes = ((int(self.screen_height/self.scale)) * (int(self.screen_width/self.scale)))
		
		
	@property
	# Returns the amount of actions
	def _n_actions(self):
		return len(self._action_set)
	
	# Returns the best action
	def best_action(self):
		return self.best()

	def _step2(self, a):
		action = self._action_set[a] # Select the action from the action dict
		self.act(action)
		ob = np.ctypeslib.as_array(self.update().contents)
		reward = self.score()
		ending = self.terminal_state()
		return ob, reward, ending, {}

	def _step(self, a):
		action = self._action_set[a] # Select the action from the action dictq
		reward = 0.0
		done = False
		for frame in range(self.frame_skip):
			self.act(action[frame])
			self.update_logic()
			reward += self.score()
			done = self.terminal_state()
			if done:
				break
		ob = np.ctypeslib.as_array(self.update_screen().contents)
		return ob, reward, done, {}

	# Renders the current state of the game, only for our visualisation purposes
	# it is not important for the learning algorithm
	def _render(self, mode=DEFAULT_RENDER_MODE, close=False):
		if not mode == RenderMode.RGB_ARRAY.value:
			img = None
			render_delay = None
			new_frame=None
			
			if mode == RenderMode.HUMAN.value:
				new_frame = self.pretty_screen().contents
			else:
				new_frame = self.screen().contents
			img = np.ctypeslib.as_array(new_frame)
			
			if mode == RenderMode.HUMAN.value:
				img = np.reshape(img, (self.screen_height, self.screen_width, 2))
				img = cv2.cvtColor(img, cv2.COLOR_BGR5652RGB)
				img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			elif mode == RenderMode.MINIMAL.value:
				img = np.reshape(img, (int(self.screen_height/self.scale), int(self.screen_width/self.scale)))
				
			render_delay = RENDER_SPEED.value
			
			if self.record_path is not None and RECORD:
				current_time = str(datetime.datetime.now().time().isoformat()).replace("/", ":")
				cv2.imwrite(self.record_path + "/sf" + current_time + ".png", img)
			
			cv2.imshow(self.game_name, img)	
			cv2.waitKey(render_delay)
		

	
	def _reset(self):
		self.reset_sf()
		# screen = self.screen().contents
		# obv = np.ctypeslib.as_array(screen)
		return 0 # For some reason should show the observation


	def write_out_stats(self , file_id=None):
		current_time = str(datetime.datetime.now().time().isoformat()).replace("/", ":")
		id = file_id if file_id else current_time
		SHIP_WON = 1 # some constant from the c interface
		keys = ["Won"]
		with open(os.path.join('gym_stats', self.game_name+"-"+id+'.csv'), 'wb') as csvfile:
			dict_writer = csv.DictWriter(csvfile, fieldnames=keys)
			dict_writer.writeheader()
			for t in self.terminal_states:
				dict_writer.writerow({"Won" : t == 1})

		self.terminal_states = []

			# ...
			# Add more rows here

		csvfile.close()

	def _close(self):
#		if self.write_stats:
#			self.write_out_stats()
		# maybe condition the stats?
#		self.write_out_stats()
		self.stop_drawing()

	# Configure the space fortress gym environment
	def _configure(self, mode=DEFAULT_RENDER_MODE, debug=False, record_path=None, no_direction=False, lib_suffix="", frame_skip=3, libpath=LIBRARY_PATH):
		self.debug = debug
		self.frame_skip = frame_skip
		self.mode = mode
		
		# Get the right shared library for the game
		if self.game == Games.SFS.value:
			libname = Games.SF.value.lower()
		elif self.game == Games.AIM.value or self.game == Games.SFC.value or self.game == Games.SF.value:  
			libname = self.game.lower()
		
		# There is no need for a window when in RGB_ARRAY mode
		if mode != RenderMode.RGB_ARRAY and mode != RenderMode.RGB_ARRAY.value:
			cv2.namedWindow(self.game_name)
		
		libname += LIBRARY_NAME
		if mode == RenderMode.HUMAN or mode == RenderMode.HUMAN.value:
			libname += "_FULL"
			
		libname += ".so"
		
		# Link the environment to the shared libraries
		self.update = ctypes.CDLL(libpath + '/'+libname).update_frame
		self.init_game = ctypes.CDLL(libpath +'/'+libname).start_drawing
		self.act = ctypes.CDLL(libpath +'/'+libname).set_key
		self.reset_sf = ctypes.CDLL(libpath +'/'+libname).reset_sf
		self.screen = ctypes.CDLL(libpath +'/'+libname).get_screen
		try:
			self.update_logic = ctypes.CDLL(libpath +'/'+libname).SF_iteration
			self.update_screen = ctypes.CDLL(libpath +'/'+libname).update_screen
			self.update_screen.restype = ctypes.POINTER(ctypes.c_ubyte * self.n_bytes)
		except:
			print("Warning: Some functions where not found in the library.")
		try:
			self.best = ctypes.CDLL(libpath +'/'+libname).get_best_move
		except:
			print("Warning: best_move function not found in the library.")

		self.terminal_state = ctypes.CDLL(libpath +'/'+libname).get_terminal_state
		self.score = ctypes.CDLL(libpath +'/'+libname).get_score
		self.stop_drawing = ctypes.CDLL(libpath +'/'+libname).stop_drawing
		self.pretty_screen = ctypes.CDLL(libpath +'/'+libname).get_original_screen
		# Configure how many bytes to read in from the pointer
		# c_ubyte is equal to unsigned char
		self.update.restype = ctypes.POINTER(ctypes.c_ubyte * self.n_bytes)
		self.screen.restype = ctypes.POINTER(ctypes.c_ubyte * self.n_bytes)

		# 468 * 448 * 2 (original size times something to do with 16 bit images)
		sixteen_bit_img_bytes = self.screen_width * self.screen_height * 2
		self.pretty_screen.restype = ctypes.POINTER(ctypes.c_ubyte * sixteen_bit_img_bytes)
		self.score.restype = ctypes.c_float

		# Initialize the game's drawing context and it's variables
		# I would rather that this be in the init method, but the OpenAI developer himself stated
		# that if some functionality of an enviroment depends on the render mode, the only way
		# to handle this is to write a configure method, a method that is only callable after the
		# init
		self.init_game()

		self.record_path = record_path

		# add down movement when in no_direction mode
		if no_direction:
			self._action_set[3] = 65364
		self.action_space = gym.spaces.Discrete(len(self._action_set))
