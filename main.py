from generator import Generator
from search import Searcher
from connectionist import Connectionist

g = Generator(2)
searcher = Searcher()
connector = Connectionist()

n = 5 # number of runs
for i in range(n):
    g.generate()
    belief_network = g.get_belief_network()
    neural_network = g.get_neural_network()

    print 'search', searcher.run(belief_network)
    print 'connector', connector.run(neural_network)



