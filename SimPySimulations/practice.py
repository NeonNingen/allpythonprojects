import simpy, random, statistics

waitTimes = [] # The list of wait times

class Theater(): # Theater Enviroment
	def __init__(self, env, numCashiers, numServers, numUshers):
		self.env = env
		self.cashier = simpy.Resource(env, numCashiers)
		self.server = simpy.Resource(env, numServers)
		self.usher = simpy.Resource(env, numUshers)

	def purchaseTicket(self, moviegoer):
		# Cashier sells the ticket in a 1 - 3 minute span
		yield self.env.timeout(random.randint(1, 3))

	def checkTicket(self, moviegoer):
		# Usher checks ticket and can do it in 3 or more seconds
		yield self.env.timeout((3 / 60))

	def sellFood(self, moviegoer):
		# Servers sell food in a 1 - 5 minute span
		yield self.env.timeout(random.randint(1, 5))


def goToMovies(env, moviegoer, theater):
	# The time when a moviegoer arrives to the theater
	arrivalTime = env.now

	# Cashier being requested from a moviegoer to buy a ticket
	with theater.cashier.request() as request:
		yield request
		yield env.process(theater.purchaseTicket(moviegoer))

	# Usher being requested from a moviegoer to check their ticket
	with theater.usher.request() as request:
		yield request
		yield env.process(theater.checkTicket(moviegoer))

	# Moviegoers have a choice to buy food from the theater
	if random.choice([True, False]):
		with theater.server.request() as request:
			yield request
			yield env.process(theater.sellFood(moviegoer))

	# The time when a moviegoer has finished setting up
	# And is ready to watch the movie
	waitTimes.append(env.now - arrivalTime)

def runTheater(env, numCashiers, numServers, numUshers):
	# Running the theater
	theater = Theater(env, numCashiers, numServers, numUshers)

	# Amount of moviegoers
	for moviegoer in range(3):
		env.process(goToMovies(env, moviegoer, theater))

	# Wait a bit before generating another moviegoer
	while True:
		yield env.timeout(0.20) # Represent 12 seconds as 12/60 = 0.20

		moviegoer += 1
		env.process(goToMovies(env, moviegoer, theater))


# Mean wait time for each moviegoer to get to their seat
# Print each result clearlys
def getAverageWaitTime(waitTimes):
	averageWait = statistics.mean(waitTimes)
	minutes, fracMinutes = divmod(averageWait, 1)
	seconds = fracMinutes * 60
	return round(minutes), round(seconds)
	

def getUserInput():
	# Configure the amount of Cahsiers, Servers and Ushers
	numCashiers = input("Input # of cashiers working: ")
	numServers = input("Input # of servers working: ")
	numUshers = input("Input # of ushers working: ")
	params = [numCashiers, numServers, numUshers]
	if all(str(i).isdigit() for i in params):
		params = [int(x) for x in params]
	else: # Defaults value back if not a integer
		print("Could not parse input. The simulation will use default values.",
			"\n1 Cashier, 1 Server, 1 Usher.",)
		params = [1, 1, 1]
	return params

def main(): 
	# Setup
	random.seed(42)
	numCashiers, numServers, numUshers = getUserInput()

	# Run Simulator
	env = simpy.Environment()
	env.process(runTheater(env, numCashiers, numServers, numUshers))
	env.run(until = 90)

	# View the Simulator Results
	mins, secs = getAverageWaitTime(waitTimes)
	print("Running simulation...", 
		f"\nThe average wait time is {mins} minutes and {secs} seconds")

if __name__ == '__main__':
	main()



