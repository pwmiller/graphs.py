'''
This module implements several algorithms on our graph structure and provides
some utility data structures.
'''

import heapq
import graph

# __unspecified is intended for use as a default keyword parameter.  We don't
# use None for this because one might want to have None as a vertex in a graph.
# Since this object is constructed in this module, it's guaranteed not to be a
# vertex in any graph, unless the end user of this library goes out of his
# way to access it -- and, in that case, said user deserves any wierd behavior
# he gets.

__unspecified = object()

class PriorityQueue (object):
    '''
    This object wraps the functionality of the heapq module into a single
    class.
    '''
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
    '''
    This is a standard union find data structure.
    '''
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
Infinity = __Infinity()

def DFS (G, v = __unspecified):
    if v not in G.vertices:
        # The following selects some arbitrary element from G.vertices
        # without converting the whole mess to a list.
        v = iter (G.vertices).next()
    neighbors = graph.toAdjacencyLists (G)
    yield v
    visited = set ([v])
    stack = neighbors [v]
    while stack:
        w = stack.pop()
        if w not in visited:
            yield w
            visited.add (w)
            stack.extend (neighbors [w])

def BFS (G, v = __unspecified):
    return NotImplemented

def Prim (G, root = __unspecified):
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

def bridges (G):
    '''
    See West, p. 23., Theorem 1.2.14. :
    An edge is a cut edge if and only if it belongs to no cycle.
    '''
    return NotImplemented

def realizeDegreeSequence (*seq):
    return NotImplemented

del __Infinity, __MinusInfinity
