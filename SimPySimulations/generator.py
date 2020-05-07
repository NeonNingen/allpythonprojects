def generator(n):
	while True:
		for j in range(n):
			yield j

def function(n):
	for j in range(n):
		return j

for i in range(0, 3):
	print(next(generator(3)))