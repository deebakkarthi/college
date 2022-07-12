from collections import deque, namedtuple


# Adjacent map implementation of an directed, unweighted graph
# Any undirected graph can be converted to a directed one
# Handle that in the implementation with two add_edge() calls
class du_graph:
    def __init__(self):
        self.map = dict()

    def add_vertex(self, u):
        # Using set() opposed to list() because set provides almost O(1)
        # "contains" operation whereas list() is O(n)
        # Though slower in some cases in terms of iteration, sets also
        # prevent duplicate edges
        self.map[u] = set()

    # add an edge from u to v
    def add_edge(self, u, v):
        self.map[u].add(v)

    def neighbours(self, u):
        return self.map[u]

    # Generator for the vertices
    def __iter__(self):
        for i in self.map:
            yield i


class dw_graph:
    def __init__(self):
        self.map = dict()

    def add_vertex(self, u):
        # Using dict as we have to store the weights to
        # the dest will be the key and weight will be the value
        # This allows self.map[u][v] to get the weight in O(1)
        # Like set this also prevents duplicate edges
        self.map[u] = dict()

    # add an edge from u to v with weight w
    def add_edge(self, u, v, w):
        self.map[u][v] = w

    def neighbours(self, u):
        return self.map[u].keys()

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
# list() is glorified C array. pop(0) costs O(n)
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
