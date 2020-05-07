from power_level import *
import random

class Battle(Saiyan):
	def __init__(self):
		super().__init__(self)
		self.attack = self.powerlevel
		self.defence = self.powerlevel
		self.hp = random.randint(1000000, 10000000)

	def opponent_randomizer(self, powerlevel2 = 0):
		self.attack = ((self.powerlevel ^ 2) / 
			random.randint(1000000, 10000000) -
			self.defence + self.hp)
		self.defence = ((self.powerlevel ^ 3) / 
			random.randint(1000000, 100000000) -
			self.attack / self.defence + self.hp) 
		return self.attack, self.defence

	def battle_randomizer(self):
		self.attack = ((self.powerlevel ^ 2) / 
			random.randint(1000000, 10000000) -
			self.defence + self.hp)
		self.defence = ((self.powerlevel ^ 3) / 
			random.randint(1000000, 100000000) -
			self.attack / self.defence + self.hp) 
		return self.attack, self.defence


	def setup(self):
		print("LET THE BATTLE BEGIN!")
		print(f"{character} VS {opponent}!")
		temp = self.battle_randomizer()
		temp2 = self.opponent_randomizer(opponent_powerlevel)
		print(temp)

	
	def fight(self):
		print("FIGHT!")



