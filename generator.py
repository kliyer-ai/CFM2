from vertex import Vertex
import numpy as np
import random

class Generator:

    def __init__(self, n_elements):
        self.n_elements = n_elements
        self.vertices = []
        self.edges = ({}, {})
        self.data_elements = {}


    def generate(self):
        n_edges = random.randint(self.n_elements / 2, self.n_elements * 2)
        n_data = self.n_elements / 4
        max_weight = 5

        vertices = []
        c_plus = {}
        c_minus = {}
        data_elements = {}

        # create vertices
        for n in xrange(self.n_elements):
            vertices.append(Vertex(n))
            
        # create edges
        for n in xrange(n_edges):
            vi, vj = random.sample(vertices, 2)
            # sort vertices in edge to make it easier to compare two eges
            edge = tuple(sorted( (vi, vj) ))
            w = random.random() * max_weight
            
            # check if edge already exists
            if edge in c_plus or edge in c_minus:
                continue

            if random.random() > 0.5:
                c_plus[edge] = w
            else:
                c_minus[edge] = w
                
        # add data elements    
        for n in xrange(n_data):
            v = random.choice(vertices)
            w = random.random() * max_weight
            data_elements[v] = w


        self.vertices = vertices
        self.edges = (c_plus, c_minus)
        self.data_elements = data_elements


    def get_belief_network(self):
        return self.vertices, self.edges, self.data_elements

    def get_neural_network(self):
        c_plus, c_minus = self.edges
        connections = np.zeros(shape=(self.n_elements, self.n_elements))

        for (vi, vj), _ in c_plus.items():
            connections[vi.n][vj.n] = 0.4
            connections[vj.n][vi.n] = 0.4

        for (vi, vj), _ in c_minus.items():
            connections[vi.n][vj.n] = -0.6
            connections[vj.n][vi.n] = -0.6

        specials = np.zeros(shape=self.n_elements)
        for v, _ in self.data_elements.items():
            specials[v.n] = 0.5
    

        return connections, specials



