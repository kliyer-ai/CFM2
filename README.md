# CFM - Group Practical 2

## Instruction
1. make sure to use python version 2.7
1. run main.py, e.g. 'python main.py'

## Things you could consider chaning for your experiments:
### main.py
* n_vertices: determines the amount of nodes in the network. 
* n: how many runs should be performed at once.
* the printing if you think it's ugly

### generator.py 
* n_edges: indicates how many edges the graph will have
* n_data: indicates how many data elements/clamped nodes/special nodes the graph will have
* max_weight: maximum weight (lel)

### conntectionist.py
* init_val: see slides; two values are possible
* threshold: see slides; two values are possible; refers to 'min change'

### Misc
* The believe network has continuous weight. However, the neural network has fixed weight (either excitatory or inhibitory). So, naturally, information gets lost which might explain the poor performance.
