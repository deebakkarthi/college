#!/usr/bin/env python
from random import randint

# Generates a random DAG
# Creates "ranks" of vertices
# The is a _chance_ for an edge from an older generation to a newer
# No connection intrageneration or in the opposite direction

ranks = randint(2,5)
# Index of the last vertex 
# Starting at 0
# Can also be taken as number of nodes in the DAG
nodes = 0
# Chance for an edge
chance = 30

for i in range(ranks):
    
    # Number of nodes generated in the new generation
    new_nodes = randint(1,5)

    # Iterating over all the nodes in the past generation
    for j in range(nodes):
        # Checking if there is a chance to connect to one of the new generation
        for k in range(new_nodes):
            if randint(0,100) < chance:
                print("{} {}".format(j,k+nodes))
    # New nodes belong to the old generation now
    nodes += new_nodes
