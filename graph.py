import itertools

def pairs (seq):
    return itertools.combinations (seq, 2)

class Graph (object):
    def __init__(self, vertices = None, edges = None):
	if vertices is not None:
	    self.__vertices = list (set (vertices))
	if edges is not None:
	    self.__edges = list (set (edges))

	for edge in self.__edges:
	    if len (edge) != 2 or \
	       edge[0] not in self.__vertices or \
	       edge[1] not in self.__vertices:
		raise TypeError, "Edges must be pairs of vertices."

    @property
    def vertices (self):
	return self.__vertices

    @property
    def edges (self):
	return self.__edges
    
    def add_vertex (self, v):
	self.__vertices.append (v)

    def add_edge (self, e):
	self.__edges.append (e)

    def adjacencies (self, v):
	return sorted (list (
            [list (set (e).symmetric_difference ( set ([v]) ))[0] \
		for e in self.edges if v in e]))

    def degree (self, v):
	return len (self.adjacencies (v))

    def degree_sequence (self):
	return sorted ( [self.degree (v) for v in self.__vertices ] )

    def degrees (self):
	return [self.degree (v) for v in self.__vertices]
    
    def min_degree (self):
	return self.degree_sequence() [0]

    def max_degree (self):
	return self.degree_sequence() [-1]
    
    def order (self):
	return len (self.__vertices)

    def size (self):
	return len (self.__edges)

    def adjacency_lists (self):
	return [ (v, G.adjacencies (v)) for v in self.__vertices ]
    
G = Graph (vertices = range (20),
	   edges = [p for p in pairs (range (20)) \
		    if p[0] * p[1] > 90 or p[0] * p[1] < 5])

