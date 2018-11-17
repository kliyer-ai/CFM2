class Vertex:
    n = 0
    
    def __init__(self):
        self.n = Vertex.n
        Vertex.n += 1
        
    def __repr__(self):
        return 'Vector ' + str(self.n)  