from battle_sys import *

plevel = Saiyan()
battlesys = Battle()

character = input("Put your character's name: ")
while True:
	user_powerlevel = int(input(f"Enter the {character} power level: "))
	if user_powerlevel > 10000000:
		print("Power level is too high\nPlease try again\n")
	else:
		print("Move on forward!\n")
		break
opponent = input("Put your opponent's name: ")
opponent_powerlevel = plevel.randomizer()

battlesys.setup()
