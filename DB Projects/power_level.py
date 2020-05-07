import random
'''
A power level system. Each Class holds a power level
Also this program gets updated when something important added
'''

class Saiyan:
	def __init__(self, powerlevel = 0):
		self.powerlevel = powerlevel
		self.multipler = 0
		

	def randomizer(self):
		self.powerlevel = random.randint(5000, 10000000)
		return self.powerlevel


	def super_saiyan(self):
		self.multipler = self.powerlevel * 50
		return self.multipler

	def super_saiyan2(self):
		self.multipler = self.powerlevel * 100
		return self.multipler

	def super_saiyan3(self):
		self.multipler = self.powerlevel * 400
		return self.multipler

	def super_saiyangod(self):
		self.multipler = self.powerlevel * 126000
		return self.multipler

	def super_saiyanblue(self):
		self.multipler = self.powerlevel * (126000 * 60)
		return self.multipler


