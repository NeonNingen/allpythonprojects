
import threading
import random
import os
import time

mutex = threading.Lock()

tree = list(open('tree3.txt').read().rstrip())

def colored_dot(color):
    if color == 'red':
        return 'cecho {0C}®{#}'
    if color == 'green':
        return 'cecho {0A}®{#}'
    if color == 'yellow':
        return 'cecho {0E}®{#}'
    if color == 'blue':
        return 'cecho {0B}®{#}'



def lights(color, indexes):
	off = True
	while True:
		for idx in indexes:
			tree[idx] = colored_dot(color) if off else '®'


		mutex.acquire()
		os.system('cls' if os.name == 'nt' else 'clear')
		cmd = ''.join(tree)
		os.system(cmd)
		mutex.release()

		off = not off

		time.sleep(random.uniform(.5, 1.5))


yellow = []
red = []
green = []
blue = []

for i, c in enumerate(tree):
	if c == "Y":
		yellow.append(i)
		tree[i] = '®'
	if c == "R":
		red.append(i)
		tree[i] = '®'
	if c == "G":
		green.append(i)
		tree[i] = '®'
	if c == "B":
		blue.append(i)
		tree[i] = '®'

ty = threading.Thread(target=lights, args=('yellow', yellow))
tr = threading.Thread(target=lights, args=('red', red))
tg = threading.Thread(target=lights, args=('green', green))
tb = threading.Thread(target=lights, args=('blue', blue))

for t in [ty, tr, tg, tb]:
	t.start()
for t in [ty, tr, tg, tb]:
	t.join()