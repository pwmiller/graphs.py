import collections

class Graph (object):
    def __init__(self, vertices = None, edges = None):
        if vertices is None:
            vertices = []
        if edges is None:
            edges = []

        self.vertices = list (set (vertices))

        for e in edges:
            if len (e) != 2 or \
                   e[0] not in self.vertices or e[1] not in self.vertices:
                raise TypeError, "%(edge)s is not a valid edge." % \
                      { 'edge' : repr (e) }

        self.edges = list (set ([frozenset (e) for e in edges]))

def fromAdjacencyMatrix (M):
    return NotImplemented

def fromAdjacencyLists (Ls):
    return NotImplemented

def toAdjacencyLists (G):
    adjacencies = {}
    for v in G.vertices:
	adjacencies [v] = []
	for (x,y) in [e for e in G.edges if v in e]:
	    if x != v:
		adjacencies[v].append (x)
	    else:
		adjacencies[v].append (y)
    return adjacencies

def toAdjacencyMatrix (G):
    return NotImplemented

def makeSimple (G):
    return NotImplemented
