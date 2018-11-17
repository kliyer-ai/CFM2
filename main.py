from generator import Generator
from search import Searcher
from connectionist import Connectionist
from vertex import Vertex

g = Generator(10)
searcher = Searcher()
connector = Connectionist()

n = 5 # number of runs
for i in range(n):
    g.generate()
    belief_network = g.get_belief_network()
    neural_network = g.get_neural_network()

    coherence, (true, false) = searcher.run(belief_network)
    print 'coherence search:', coherence
    print 'accepted propositions:', sorted(true, key=lambda v: v.n)
    print 'rejected propositions:', sorted(false, key=lambda v: v.n)
    print '-----------------------------------------------'

    activations, harmony = connector.run(neural_network)
    print 'harmony', harmony
    true = []
    false = []
    for i, a in enumerate(activations):
        if a == 1:
            true.append(Vertex(i))
        else:
            false.append(Vertex(i))
    print 'accepted propositions:', sorted(true, key=lambda v: v.n)
    print 'rejected propositions:', sorted(false, key=lambda v: v.n)

    print '#################################################'
    print '#################################################'



