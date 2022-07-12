from collections import deque, namedtuple
import heapq


# Since sorted(pq, key:lamda x: x[2]) or
# find_cluster(x[1]) != find_cluster(x[2])
# are not very readable
edge = namedtuple("edge", ["src", "dest", "weight"])


# storing infinity in a constant as writing is float('inf') is tedious
INF = float('inf')


# Adjacent map implementation of an directed, unweighted graph
# Any undirected graph can be converted to a directed one
# Handle that in the implementation with two add_edge() calls
class du_graph:
    def __init__(self):
        self.map = dict()

    def order(self):
        return len(self.map)

    # pseudo root. Starting point for prim's
    def root(self):
        return next(iter(self.map))

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

    # List of vertices who have a edge directed to u
    def indegree(self, u):
        tmp = list()
        for v, e in self.map.items():
            if u in e:
                tmp.append(v)
        return tmp

    def get_edges(self):
        edge_list = list()
        for i in self:
            for j in self.map[i]:
                edge_list.append(edge(i, j))
        return edge_list

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

    # pseudo root. Starting point for prim's
    def root(self):
        return next(iter(self.map))

    def order(self):
        return len(self.map)

    # add an edge from u to v with weight w
    def add_edge(self, u, v, w):
        self.map[u][v] = w

    # List of vertices who have a edge directed from u
    def neighbours(self, u):
        return self.map[u].keys()

    def weight(self, u, v):
        return self.map[u][v]

    # List of vertices who have a edge directed to u
    def indegree(self, u):
        tmp = list()
        for v, e in self.map.items():
            if u in e:
                tmp.append(v)
        return tmp

    def get_edges(self):
        edge_list = list()
        for i in self:
            for j in self.map[i]:
                edge_list.append(edge(i, j, self.map[i][j]))
        return edge_list

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


# Topological sort (Works only on directed acyclic graphs)
# u->v is an edge then u should appear before(may or maynot be consecutive)
# v in the order, the first elements to appear are elements with 0
# indegree edges.
def topo(g):
    indegree = dict()
    # Queue of vertices with indegree of 0
    ready = deque()
    order = set()
    for i in g:
        indegree[i] = len(g.indegree(i))
        if indegree[i] == 0:
            ready.append(i)
    while ready:
        tmp = ready.popleft()
        order.add(tmp)
        for i in g.neighbours(tmp):
            # Reducing the dependency as tmp is added to the order. So it's
            # neighbours are free to enter the order as well
            indegree[i] -= 1
            # If it doesn't have any other dependencies add to ready queue
            if indegree[i] == 0:
                ready.append(i)
    return order


# given a list of sets, returns the set with the element u
def get_cluster(cluster, u):
    for i in cluster:
        if u in i:
            return i
    return None


# merges two clusters and removes the og two
def merge_cluster(cluster, u, v):
    tmp = u.union(v)
    cluster.remove(u)
    cluster.remove(v)
    cluster.append(tmp)


# generates MST of an undirected, weighted graph
def kruskal(g):
    # list of edges in the mst
    mst = list()
    req_size = g.order()-1

    # Priority Queue with weight as the key
    pq = g.get_edges()
    pq = sorted(pq, key=lambda x: x.weight)

    # Cluster generation
    cluster = list()
    for i in g:
        cluster.append({i})

    # Traversing the whole edge list instead of checking the usual condition
    # len(mst) <= g.order()-1 as either we have use a deque to popleft() or
    # keep an external index var. Instead checking after each insertiont to mst
    for i in pq:
        u = get_cluster(cluster, i.src)
        v = get_cluster(cluster, i.dest)
        # If they belong to different clusters
        if u != v:
            mst.append(i)
            merge_cluster(cluster, u, v)
            if len(mst) == req_size:
                break

    return mst


# return all the vertices of a undirected set of edges
def span(edge_list):
    vertices = set()
    for i in edge_list:
        vertices.add(i.src)
        vertices.add(i.dest)
    return vertices


# Calc cost of a set of edges
def cost(edge_list):
    ret = 0
    for i in edge_list:
        ret += i.weight
    return ret


def update_pq(pq, u, weight, edge):
    for i in pq:
        if i[1][0] == u:
            i[0] = weight
            i[1][1] = edge
            return


# Prim's algorithm for MST of undirected, weighted graph
def prim(g):
    mst = set()
    # Contains the shortest distance to a vertex from the formed MST
    # as MST is empty at first these are INF
    d = dict()
    pq = list()
    for i in g:
        d[i] = INF
    # We are picking one element to be in the MST first. By setting the weight
    # to 0 we can pop it first. This simulates starting from this point and
    # picking the smallest from there
    d[g.root()] = 0
    for i in d:
        # PQ is a triplet of the form
        # Shortest distance from MST to vertex,
        # vertex
        # The edge with the shortest distance
        # Initially edge is None as we don't have any connection with MST
        pq.append([d[i], [i, None]])
    pq = sorted(pq, key=lambda x: x[0])
    while pq:
        # Removing the vertex closest to the MST
        key, value = pq.pop(0)
        u, e = value
        # If there is actually and edge from MST to u, then connect it
        if e is not None:
            mst.add(e)
        # Since u is in the MST now, we have to update all weights.
        # d contains the shortest distance to the MST.
        # since we added a new vertex we have to check if this changes anything
        for v in g.neighbours(u):
            wgt = g.weight(u, v)
            if wgt < d[v]:
                d[v] = wgt
                update_pq(pq, v, wgt, edge(u, v, wgt))
        pq = sorted(pq, key=lambda x: x[0])
    return mst
