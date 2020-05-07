# Context Managers and the with Statement P3

from contextlib import contextmanager

@contextmanager
def managed_file(name):
	try:
		f = open(name, 'w')
		yield f
	finally:
		f.close()

with managed_file('hello.txt') as f:
	f.write('Hello, world!\n')
	f.write('Bye now!')