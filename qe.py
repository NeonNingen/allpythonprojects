# https://2017.integralmaths.org (Quadratic Equation Formula)
# A. B and C are whole numbers
import math, zain

A = input("Input A: ")
A = zain.checkNum(A)
B = input("Input B: ")
B = zain.checkNum(B)
C = input("Input C: ")
C = zain.checkNum(C)

D = (B**2 - 4*A*C)
if D >= 0:
	print(round((-B + math.sqrt(D)) / (2*A), 10))
	print(round((-B - math.sqrt(D)) / (2*A), 10))
else:
	print("No real roots")