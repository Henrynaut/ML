import numpy as np
import random
random.seed(200)

#Create Sigmoid Function
def sig(inp):
    return (1/(1+np.exp(-1*inp)))

#For Back Propagation, make Desigmoid function
def dsig(inp):
    return (1.0-inp)*inp