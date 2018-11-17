class Searcher:

    def run(self, network):
        vertices, (c_plus, c_minus), data_elements = network

        frontier = []
        initial_state = (vertices, [], [])

        # add initial state to frontier
        frontier += self.generate_successors(initial_state)

        best = (0, None)


        while frontier:
            state = frontier.pop()
            coh = self.evaluate(state, c_plus, c_minus, data_elements)
            
            if coh > best[0]:
                _, true, false = state
                best = (coh, (true, false) )    
            
            frontier += self.generate_successors(state)
            
        return best


    def generate_successors(self, state):
        vertices, true, false = state
        vertices = list(vertices) # copy list of vertices
        
        # no new states can be generated 
        if not vertices:
            return []
        
        v = vertices.pop()
        return [ ( vertices, true + [v], false ) , ( vertices, true, false + [v] ) ]


    def evaluate(self, state, c_plus, c_minus, data_elements):
        vertices, true, false = state
        
        # not all elements have a true value yet
        if vertices:
            return 0
        
        coh = 0
        # consistent elements
        for (vi, vj), w in c_plus.items():
            if vi in true and vj in true:
                coh += w
        
        # inconsistent elements
        for (vi, vj), w in c_minus.items():
            if vi in true and vj in false or vi in false and vj in true:
                coh += w
                
        # data elements
        for v, w in data_elements.items():
            if v in c_plus:
                coh += w
                
        return coh