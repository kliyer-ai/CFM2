# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:08:02 2018

@author: Bart
"""

import numpy as np

def harmony(activations):
    harmony = 0
    for i in range(len(activations)):
        harmony += activations[i] * np.sum(activations * connections[i])
    return harmony

def create_randomly(dim):
    dim = len(activations)
    connections = np.random.choice([0, 0.4, -0.6], (dim, dim))
    np.fill_diagonal(connections, 0)
    for i in range(dim):
        for j in range(dim):
            if i > j:
                connections[i][j] = connections[j][i]
    specials = np.random.choice([0, 0.5], dim, p = [0.9, 0.1])
    return (connections, specials)

def update(activations, connections, specials, d, max, threshold):
    converged = True
    new_activations = []
    for i in range(len(activations)):
        new_activations.append(activations[i] * (1-d))
        net = np.sum(activations * connections[i]) + specials[i]
        if net > 0:
            new_activations[i] += net * (max-activations[i])
        else:
            new_activations[i] += net * (activations[i]-min)
        new_activations[i] = np.tanh(new_activations[i])
        if np.abs(new_activations[i] - activations[i]) > threshold:
            converged = False
    return new_activations, converged

def discretise(activations):
    return np.sign(activations)
        
d = 0.05                            # decay rate
dim = 10                            # number of nodes
init_val = 0.1                      # initial activations of nodes
activations = [init_val] * dim      # list of activations of nodes
max = 1                             # max value of nodes
min = -1                            # min value of nodes
threshold = 0.01                    # convergence threshold
done = False                        # keeps track of convergence
connections, specials = create_randomly(dim)  # matrix of connections between nodes
                                              # special nodes biasing specific nodes (not considered in calculating harmony)

while not done:
    activations, done = update(activations, connections, specials, d, max, threshold)
    print activations
    print harmony(activations)

activations = discretise(activations)
print "final activations and harmony:"
print activations
print harmony(activations)