import heapq
import graph

# Some data structures and utility objects.

class PriorityQueue (object):
    def __init__(self, data):
        self.__data = []
        data = list (data)
        self.__data.extend (data)
        heapq.heapify (self.__data)

    def add (self, item):
        heapq.heappush (self.__data, item)

    def extract_min (self):
        return heapq.heappop (self.__data)

    def __contains__(self, item):
        return item in self.__data

    def __len__(self):
        return len (self.__data)

class UnionFind (object):
    def __init__(self):
        self.parent = {}
        self.rank   = {}

    def makeSet (self, x):
        self.parent [x] = x
        self.rank [x] = 0

    def find (self, x):
        parent = self.parent
        if parent[x] == x:
            return x
        else:
            parent[x] = self.find (parent[x])
            return parent[x]

    def union (self, x, y):
        rank = self.rank
        parent = self.parent

        xRoot = self.find (x)
        yRoot = self.find (y)
        if rank [xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        elif rank [xRoot] < rank [yRoot]:
            parent[xRoot] = yRoot
        elif xRoot != yRoot:
            parent[yRoot] = xRoot
            rank [xRoot] += 1


class __Infinity (object):

    '''Instances X of this class satisfy X > Y for all Y.'''

    def __lt__(self, other):
        #pylint: disable-msg=w0613
        #pylint: disable-msg=r0201
        return False

    def __gt__(self, other):
        #pylint: disable-msg=w0613
        #pylint: disable-msg=r0201
        return True

Infinity = __Infinity()

class __MinusInfinity (object):
    ''' Instances X of this class satisfy X < Y for all Y. '''

    def __lt__(self, other):
        #pylint: disable-msg=w0613
        #pylint: disable-msg=r0201
        return True

    def __gt__(self, other):
        #pylint: disable-msg=w0613
        #pylint: disable-msg=r0201
        return False

MinusInfinity = __MinusInfinity()

del __Infinity, __MinusInfinity

def DFS (G, v = None):
    if v not in G.vertices:
        v = G.vertices[0]
    neighbors = graph.toAdjacencyLists (G)
    yield v
    visited = set ([v])
    S = neighbors [v]
    while S:
        w = S.pop()
        if w not in visited:
            yield w
            visited.add (w)
            S.extend (neighbors [w])

def BFS (G, v):
    return NotImplemented

def Prim (G, root = None):
    if root not in G.vertices:
        root = G.vertices[0]
    key = {}
    Pi = {}
    adj = graph.toAdjacencyLists(G)
    for u in G.vertices:
        key [u] = Infinity
        Pi [u] = None
    key [root] = 0
    Q = PriorityQueue (G.vertices)
    while Q:
        u = Q.extract_min()
        for v in adj[u]:
            if v in Q and G.weight ( (u, v) ) < key [v]:
                Pi [v] = u
                key[v] = G.weight ( (u, v) )
    return [(v, Pi[v]) for v in G.vertices if v is not root]

def Kruskal (G):
    weight = G.weight
    T = set ([])
    U = UnionFind()
    Q = PriorityQueue([(weight (e), tuple(e)) for e in G.edges])
    for v in G.vertices:
        U.makeSet (v)

    while Q:
        (w, (u, v)) = Q.extract_min()
        if U.find (u) != U.find (v):
            T.add ( (u, v) )
            U.union (u, v)
    return T
