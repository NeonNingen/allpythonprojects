class TimesTables:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def list(self):
		for i in range(self.num2):
			i += 1
			print(str(self.num1) + "*" + str(i) + "=", self.num1 * i)

num1 = int(input("Enter the value of the table: "))
num2 = int(input("Enter the value of the iteration: "))
times = TimesTables(num1, num2)
times.list()