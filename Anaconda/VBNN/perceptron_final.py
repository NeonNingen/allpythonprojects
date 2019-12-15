import numpy as np

def sigmoid(x):
    return 1 / (1 * np.exp(-x))    # Sigmoid Function

def sigmoid_derivative(x):         # Sigmoid Gradient
    return x * (1 - x)

training_inputs = np.array([[0, 0, 1],        # Input Values
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T      # Output answers

np.random.seed(1)     # Random Weights

synaptic_weights = 2 * np.random.random((3, 1)) - 1 # Array of Random Weights

print("Random starting synaptic weights: ")
print(synaptic_weights)

for iteration in range(2000):
    input_layer = training_inputs 
    outputs = sigmoid(np.dot(input_layer, synaptic_weights)) # Sigmoid Function
    error = training_outputs - outputs    # Calculate the errors
    adjustments = error * sigmoid_derivative(outputs)   # Fixing the weights to our desire
    synaptic_weights += np.dot(input_layer.T, adjustments) # New Weights

print("Synaptic weights after training: ")
print(synaptic_weights)

      
print("Outputs after training: ")
print(outputs)
