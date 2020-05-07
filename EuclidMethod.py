import zain

X = input("Input X: ")
X = zain.checkNum(X)
Y = input("Input Y: ")
Y = zain.checkNum(Y)
while X != Y:
	if X > Y:
		X = X - Y
	else:
		Y = Y - X
print(X, Y)
print("HCF = ", X)