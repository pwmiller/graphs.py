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
    return NotImplemented

def toAdjacencyMatrix (G):
    return NotImplemented

def makeSimple (G):
    return NotImplemented
