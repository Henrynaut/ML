import numpy as np
import random
random.seed(200)

# Create Sigmoid Function
def sig(inp):
    return (1/(1+np.exp(-1*inp)))

# For Back Propagation, make Desigmoid function
def dsig(inp):
    return (1.0-inp)*inp

# Define class for neuron
class Neuron:
    def __init__(self,weights,func,dfunc):
        # member variables for class
        self.weights = weights
        self.output = None
        self.func = func
        # dfunc is the derivative of the function
        self.dfunc = dfunc
        # No delta yet because we haven't defined anything
        self.delta = None
    def agr(self,x):
        bias = self.weights[-1]
        out = np.inner(self.weights.copy()[:-1],x) + bias
    def activation(self,inp):
        self.output = self.func(inp)
        return self.output

# Definition for weights
def gen_weights(dim):
    # Add 1 to the dimension for the bias
    return np.random.uniform(-0.1,0.1,dim+1)

# Definition of the actual network
# Activations correspond to activation funcitons used
def gen_net(structure, activations):
    # Create empty list
    net = []
    for i in range(1,len(structure)):
        layer = []
        for j in range(structure[i]):
            # feed in neuron weights from last layer
            weights = gen_weights(structure[i-1])
            layer.append(Neuron(weights, activations[0][i-1], activations[1][i-1]))
        net.append(layer)
    return net

# Define feed forward
def feed_fwd(net, inp):
    # It stores the current input associated with the given layer
    inp_store = inp
    for layer in net:
        out_of_curr_layer = []
        for neuron in layer:
            # Calculate accumulated output value
            accum = neuron.agr(inp_store)
            output = neuron.activation(accum)
            # Store output for later use
            out_of_curr_layer.append(output)
        inp_store = out_of_curr_layer
    return inp_store

# Define back propagation
def back_prop(net, target):
    back_len = len(net)
    for i in range(back_len):
        ind = back_len-i-1
        layer = net[ind]
        errors = []
        if ind == back_len-1:
            j=0
            for neuron in layer:
                errors.append(target[j]-neuron.output)
                j+=1
        else:
            for j in range(len(layer)):
                error = 0.0
                # For neuron in front of current neuron, check deltas
                for neuron in net[ind+1]:
                    error+=(neuron.weights[j]*neuron.delta)
                errors.append(error)
        j=0
        for neuron in layer:
            neuron.delta = errors[j]*neuron.dfunc(neuron.output)
            j+=1