from collections import deque


# Adjacent map implementation of an undirected, unweighted graph
class uu_graph:
    def __init__(self):
        self.map = dict()

    def add_vertex(self, u):
        self.map[u] = set()

    # add an edge between u and v
    def add_edge(self, u, v):
        self.map[u].add(v)
        self.map[v].add(u)

    def neighbours(self, u):
        return self.map[u]

    # Generator for the vertices
    def __iter__(self):
        for i in self.map:
            yield i


# DFS
# vis is set of visited vertices
def dfs(g, u, vis):
    vis.add(u)
    for i in g.neighbours(u):
        if i not in vis:
            dfs(g, i, vis)


# BFS
# Using deque as a queue
# deque provides O(1) insertion and deletion as it is a DLL
# list() is glorified C arrays.pop(0) costs O(n)
def bfs(g, u):
    queue = deque()
    queue.append(u)
    vis = set()
    while queue:
        tmp = queue.popleft()
        vis.add(tmp)
        for i in g.neighbours(tmp):
            if i not in vis:
                queue.append(i)
    return vis
