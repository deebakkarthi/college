#!/usr/bin/env python3
from graph import *

edges = list()
vertices = set()
while True:
    try:
        tmp = input()
        tmp = tmp.split()
        tmp = [int(x) for x in tmp]
        for i in tmp:
            vertices.add(i)
        edges.append(tmp)
    except EOFError:
        break

graph = dw_graph()
for i in vertices:
    graph.add_vertex(i)

for i in edges:
    graph.add_edge(i[0], i[1], 1)

for i in graph:
    vis = set()
    dfs(graph, i, vis)
    print(i, vis)
