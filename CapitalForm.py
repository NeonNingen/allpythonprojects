class Captials:
	def __init__(self):
		pass

	def captialform(self, s):
		for i in s:
			print(i.capitalize(),end = " ")

letters = Captials()
letters.captialform(input("Input a name: ").split(' '))
