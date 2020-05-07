def infinite_sequence():
	num = 0
	while True:
		yield num
		num += 1

gen = infinite_sequence()

i = 0
while i < 10:
	print(next(gen))
	i += 1

print(gen)