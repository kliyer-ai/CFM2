# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:08:02 2018

@author: Bart
"""

import numpy as np

class Connectionist:

    def __init__(self, d = 0.05, init_val = 0.1,  maximum = 1, minimum = -1, threshold = 0.01, max_time = 200):
        self.d = d                                        # decay rate
        self.init_val = init_val                          # initial activations of nodes
        self.max = maximum                                # max value of nodes
        self.min = minimum                                # min value of nodes
        self.threshold = threshold                        # convergence threshold
        self.max_time = max_time
    

    def harmony(self, activations, connections):
        harmony = 0
        for i in range(len(activations)):
            harmony += activations[i] * np.sum(activations * connections[i])
        return harmony

    """
    def create_randomly(self):
        dim = self.dim
        connections = np.random.choice([0, 0.4, -0.6], (dim, dim))
        np.fill_diagonal(connections, 0)
        for i in range(dim):
            for j in range(dim):
                if i > j:
                    connections[i][j] = connections[j][i]
        specials = np.random.choice([0, 0.5], dim, p = [0.9, 0.1])
        return (connections, specials)
    """


    def update(self, activations, connections, specials):
        converged = True
        dim = specials.size
        new_activations = []

        for i in range(dim):
            new_activations.append(activations[i] * (1-self.d))
            net = np.sum(activations * connections[i]) + specials[i]

            if net > 0:
                new_activations[i] += net * (self.max-activations[i])
            else:
                new_activations[i] += net * (activations[i]-self.min)

            if new_activations[i] > self.max:
                new_activations[i] = self.max
            if new_activations[i] < self.min:
                new_activations[i] = self.min
            # new_activations[i] = np.tanh(new_activations[i])
            if np.abs(new_activations[i] - activations[i]) > self.threshold:
                converged = False
        return new_activations, converged


    def discretise(self, activations):
        for i in range(len(activations)):
            if activations[i] > 0:
                activations[i] = self.max
            else:
                activations[i] = self.min
        return np.sign(activations)
            
    
    def run(self, network):
        connections, specials = network 
        dim = specials.size
        activations = [self.init_val] * dim # initialize activations
        
        for i in range(self.max_time):
            activations, done = self.update(activations, connections, specials)
            if done:
                break

        activations = self.discretise(activations)
        harmony = self.harmony(activations, connections)

        return activations, harmony