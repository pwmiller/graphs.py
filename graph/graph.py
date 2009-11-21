'''
The \code{graph} module implements the graph data structure itself,
as well as functions for converting graph structures to and from
the adjacency list and adjacency matrix representations.
'''

import sympy

class Graph (object):
    def __init__(self, vertices = None, edges = None):
        if vertices is None:
            vertices = []
        if edges is None:
            edges = []
	    
        self.vertices = set (vertices)

        for e in edges:
            e = tuple (sorted (e))
            if len (e) != 2 or \
                   e[0] not in self.vertices or e[1] not in self.vertices:
                raise TypeError, "%(edge)s is not a valid edge." % \
                      { 'edge' : repr (e) }

        self.edges = set ([frozenset (e) for e in edges])

def fromAdjacencyMatrix (M):
    M = sympy.matrices.Matrix (M)
    if M != M.transpose():
        raise ValueError, "The adjacency matrix of a graph must be symmetric."
    n = M.shape[0]
    return Graph (vertices = range (n), edges = \
               [ (x,y) for x in range (n) for y in range (n) if M[x,y] != 0])

def fromAdjacencyLists (Ls):
    Ls = dict (Ls)
    vertices = []
    edges = []
    for v, neighbors in Ls:
        vertices.append (v)
        for u in neighbors:
            edges.append (u, v)
    return Graph (vertices = vertices, edges = edges)

def toAdjacencyLists (G):
    adjacencies = {}
    for v in G.vertices:
        adjacencies [v] = []
        for (x, y) in [e for e in G.edges if v in e]:
            if x != v:
                adjacencies[v].append (x)
            else:
                adjacencies[v].append (y)
    return adjacencies

def toAdjacencyMatrix (G):
    n = len (G.vertices)
    M = sympy.matrices.zeros (n)
    for (u, v) in G.edges:
        M[u, v] = M[v, u] = 1
    return M

def toDotString (G):
    return NotImplemented
