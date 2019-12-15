import numpy as np

a = np.zeros(3)
print(a)

z = np.zeros(10)
print(z)

z.shape

z.shape = (10, 1)
print(z)

z = np.ones(10)
print(z)

z = np.empty(3)
print(z)

z = np.linspace(2, 10, 5) #From 2 to 10, with 5 elements
print(z)

z = np.array([10, 20])
print(z)

a_list = [1,2,3,4,5,6,7]
z = np.array([a_list])
print(z)

b_list = ([9,8,7,6,5,4,3],[1,2,3,4,5,6,7])
z = np.array([b_list])
print(z)

z.shape
print(z.T)

np.random.seed(0)
z1 = np.random.randint(10, size = 6)
print(z1)