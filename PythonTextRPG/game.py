#Basic Python RPG

import cmd
import textwrap
import sys
import os
import time
import random


screen_width = 100

# Player Setup!
class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.location = 'start'

# Title Screen
def title_screen_selections():
	while True:
		option = input('> ')
		if option.lower() == 'play':
			print('0')
			# start_game()
		elif option.lower() == 'help':
			help_menu()
		elif option.lower() == 'quit':
			sys.exit()
		else:
			print("Please enter a valid command.")


def title_screen():
	os.system('cls')
	print('##################################')
	print("# Welcome to the Classic Text RPG ")
	print('##################################')
	print("             -- Play --			 ")
	print("             -- Help --			 ")
	print("             -- Quit --			 ")
	print("      Copyright 2019 Simple.co    ")
	title_screen_selections()


def help_menu():
	print('##################################')
	print("# Welcome to the Classic Text RPG ")
	print('##################################')
	print("-- Use up, down, left, right to move")
	print("-- Type your commands to do them  ")
	print("-- Use 'look' to inspect something")
	print("-- Good luck and have fun         ")
	title_screen_selections()

# Game Functionality
def start_game():

# Map
def map():
	


def main():
	myPlayer = player()
	title_screen()

main()