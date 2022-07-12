#!/usr/bin/env python3
from graph import *

edge_list = list()
vertices = set()
while True:
    try:
        # One liner to get input and create a namedtuple edge
        tmp = edge(*[int(x) for x in input().split()])
        vertices.add(tmp.src)
        vertices.add(tmp.dest)
        edge_list.append(tmp)
    except EOFError:
        break

graph = dw_graph()
for i in vertices:
    graph.add_vertex(i)

for i in edge_list:
    graph.add_edge(i.src, i.dest, i.weight)
