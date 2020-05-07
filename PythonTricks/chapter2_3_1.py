# Context Managers and the with Statement P1

with open('hello.txt', 'w') as f:
	f.write('hello, world!')
	f.close()