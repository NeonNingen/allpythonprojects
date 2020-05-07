import simpy

def main():
	env = simpy.Environment()
	env.process(trafficLight(env))
	env.run(until = 120)
	print("Simulation Complete!")

def trafficLight(env):
	while True:
		print("Light turned GRN at t = " + str(env.now))
		yield env.timeout(30)
		print("Light turned YEL at t = " + str(env.now))
		yield env.timeout(5)
		print("Light turned RED at t = " + str(env.now))
		yield env.timeout(20)

if __name__ == '__main__':
	main()