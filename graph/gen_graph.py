#!/usr/bin/env python
from random import randint
import sys

# Global const
MIN_RANK = 3
MAX_RANK = 5
# Number of vertices /  rank
MIN_VERT = 1
MAX_VERT = 5
CHANCE = 30


def dag():
    # Generates a random DAG
    # Creates "ranks" of vertices
    # The is a _chance_ for an edge from an older generation to a newer
    # No connection intrageneration or in the opposite direction

    ranks = randint(MIN_RANK, MAX_RANK)
    nodes = 0

    for i in range(ranks):
        # Number of nodes generated in the new generation
        new_nodes = randint(MIN_VERT, MAX_VERT)

        # Iterating over all the nodes in the past generation
        for j in range(nodes):
            # Checking if there is a chance to connect to one of the new gen
            for k in range(new_nodes):
                if randint(0, 100) < CHANCE:
                    print("{} {}".format(j, k+nodes))
        # New nodes belong to the old generation now
        nodes += new_nodes


def dcg():
    # Random Cyclic graph generator
    # Same as dag but we also have a chance for backward edges
    ranks = randint(MIN_RANK, MAX_RANK)
    nodes = 0
    chance = 30

    for i in range(ranks):
        new_nodes = randint(MIN_VERT, MAX_VERT)

        for j in range(nodes+1):
            for k in range(new_nodes):
                if randint(0, 100) < CHANCE:
                    print("{} {}".format(j, k+nodes))
                else:
                    # Same logic but connect to previous gen
                    for x in range(i):
                        if randint(0, 100) < CHANCE:
                            print("{} {}".format(j, x))
        nodes += new_nodes


def usage():
    print("Usage: gen_graph -c|-a")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    if sys.argv[1] == "-c":
        dcg()
    elif sys.argv[1] == "-a":
        dag()
    else:
        usage()
