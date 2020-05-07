import random, pyautogui, math, time

time.sleep(2)

for i in range(0, 10):
	rotation = random.randint(0, 3)
	if rotation == 0:
		pyautogui.press('w')
		rotation = random.randint(0, 3)
	elif rotation == 1:
		pyautogui.press('a')
		rotation = random.randint(0, 3)
	elif rotation == 2:
		pyautogui.press('d')
		rotation = random.randint(0, 3)
	elif rotation == 3:
		pyautogui.press('s')
		rotation = random.randint(0, 3)

pyautogui.press('p')

