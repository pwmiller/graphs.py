class Vertex (object):
    def __init__(self, value):
	self.value = value

    def __str__(self):
	return self.value.__str__()

    def __cmp__(self, other):
	if other.__class__ == self.__class__:
	    return cmp (self.value, other.value)
	else:
	    return cmp (self.value, other)

class Edge (object):
    def __init__(self, head, tail, directed=False):
	self.head = head
	self.tail = tail
	self.directed = directed

class Graph (object):
    def __init__(self, vertices = None, edges = None):
	pass

