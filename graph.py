class Graph (object):
    def __init__(self, vertices = None, edges = None, directed = False):
	if vertices is None:
	    vertices = []
	if edges is None:
	    edges = []

	self.directed = directed
	self.vertices = list (set (vertices))

	for e in edges:
	    if len (e) != 2 or \
		   e[0] not in self.vertices or e[1] not in self.vertices:
		raise TypeError, "%(edge)s is not a valid edge." % \
		      { 'edge' : repr (e) } 

	if directed:
	    self.edges = list (set ([tuple (e) for e in edges]))
	else:
	    self.edges = list (set ([frozenset (e) for e in edges]))
