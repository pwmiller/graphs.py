'''
This module implements several algorithms on our graph structure and provides
some utility data structures.
'''

import collections
import heapq
import graph


class __Unspecified(object):
    '''
    This class only exists to make one instance, called \code {unspecified}.
    The object \code {unspecified} is used as a default keyword parameter in
    place of the ubiquitous \code {None}, so we can meaninfully use
    \code {None} as a vertex in a graph.
    '''

    def __repr__(self):
        return "unspecified"


unspecified = __Unspecified()
del __Unspecified

def arbitraryElementOf(container):
    '''
    Selects some arbitrary element of \code {container} (which need
    not be indexable -- \textit {e.g.\} a set or generator.
    '''
    try:
        return iter(container).next()
    except StopIteration:
        raise IndexError("No item in container to select.")


class PriorityQueue (object):
    '''
    This object wraps the functionality of the heapq module into a single
    class.
    '''

    def __init__(self, data):
        self.__data = []
        data = list(data)
        self.__data.extend(data)
        heapq.heapify(self.__data)

    def add(self, item):
        '''
        Add an item to the queue.
        '''
        heapq.heappush(self.__data, item)

    def extract_min(self):
        '''
        Find and return the item in the queue with minimum priority,
        removing it from the queue.
        '''
        return heapq.heappop(self.__data)

    def __contains__(self, item):
        return item in self.__data

    def __len__(self):
        return len(self.__data)


class UnionFind (object):
    '''
    This is a standard union find data structure.  We implement path
    compression and union by rank to obtain amortized asymptotic
    performance of $\mathcal{O}(\alpha (n))$, where $\alpha$ is the
    inverse Ackermann function.  In practice, we can basically assume
    $\alpha (n) \leq 5$, so this is effectively amortized constant-time
    performance.
    '''

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self, x):
        '''
        Adds the set $\{x\}$ to the data structure.
        '''
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        '''
        Returns the set containing $x$.
        '''
        parent = self.parent
        if parent[x] == x:
            return x
        else:
            parent[x] = self.find(parent[x])
            return parent[x]

    def union(self, x, y):
        '''
        Merges the sets containing $x$ and $y$ into a single set.
        '''
        rank = self.rank
        parent = self.parent

        xRoot = self.find(x)
        yRoot = self.find(y)
        if rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        elif rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif xRoot != yRoot:
            parent[yRoot] = xRoot
            rank[xRoot] += 1


MinusInfinity = float('-inf')
Infinity = float('+inf')


def DFS(G, start=unspecified):
    '''
    This is a generator that yields vertices from the vertex set of graph
    $G$ in the order they are encountered in a depth-first search of $G$
    starting from the vertex \code{start} (if specified) or from some
    arbitrary vertex in \code {G.vertices} if \code {start} is not
    specified.
    '''
    if start is unspecified:
        start = arbitraryElementOf(G.vertices)

    neighbors = graph.adjacencyLists(G)
    yield start
    visited = set([start])
    stack = neighbors[start]
    while stack:
        w = stack.pop()
        if w not in visited:
            yield w
            visited.add(w)
            stack.extend(neighbors[w])


def BFS(G, start=unspecified):
    '''
    This is a generator that yields the vertices of $G$ in the order
    they are encountered during a breadth-first search of $G$ starting at the
    vertex \code {start} (if specified), or starting at some arbitrary vertex
    in \code {G.vertices} if not specified.
    '''
    if start is unspecified:
        start = arbitraryElementOf(G.vertices)

    neighbors = graph.adjacencyLists(G)

    reached = collections.deque()
    searched = set()

    reached.append(start)
    while not reached.empty():
        v = reached.popleft()
        yield v
        for w in neighbors[v]:
            if w not in searched and w not in reached:
                reached.append(w)
        searched.add(v)


def Prim(G, root=unspecified):
    '''
    Returns the edges of a minimum-weight spanning tree of $G$,
    starting from the vertex \code {root} (if specified).
    '''
    if root is unspecified:
        root = arbitraryElementOf(G.vertices)
    key = {}
    Pi = {}
    adj = graph.adjacencyLists(G)
    for u in G.vertices:
        key[u] = Infinity
        Pi[u] = None
    key[root] = 0
    Q = PriorityQueue(G.vertices)
    while Q:
        u = Q.extract_min()
        for v in adj[u]:
            if v in Q and G.weight((u, v)) < key[v]:
                Pi[v] = u
                key[v] = G.weight((u, v))
    return [(v, Pi[v]) for v in G.vertices if v is not root]


def Kruskal(G, weight=None):
    '''
    Returns the vertices of a minimum-weight spanning tree of $G$
    obtained by the algorithm of Kruskal.
    '''
    if weight is None:
        def weight(edge): return 1
    T = set([])
    U = UnionFind()
    Q = PriorityQueue([(weight(e), tuple(e)) for e in G.edges])
    for v in G.vertices:
        U.makeSet(v)

    while Q:

        # pylint complains that we don't use the variable \code{w},
        # but it's really only there so we can unpack the (weight, edge)
        # tuple extracted from the queue in a nice way.  The following
        # comment is to silence pylint's complaining:

        # pylint: disable-msg=W0612

        (w, (u, v)) = Q.extract_min()
        if U.find(u) != U.find(v):
            T.add((u, v))
            U.union(u, v)
    return T


def bridges(G):
    '''
    See West, p. 23., Theorem 1.2.14. :
    An edge is a cut edge if and only if it belongs to no cycle.
    '''
    return NotImplemented


def realizeDegreeSequence(*seq):
    '''
    Returns a graph $G$ such that \code {degreeSequence (G) == sorted (seq)}
    if \code {sorted (seq)} is a graphical degree sequence.  We use the
    standard algorithm based on the Havel-Hakimi theorem.
    '''
    return NotImplemented
