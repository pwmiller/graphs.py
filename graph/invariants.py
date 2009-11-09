from algorithms import DFS

def degrees (G):
    return [ len ([e for e in G.edges if v in e]) for v in G.vertices]

def degreeSequence (G):
    return sorted (degrees (G))

def minDegree (G):
    return min (degrees (G))

def maxDegree (G):
    return max (degrees (G))

def is_regular (G):
    return minDegree (G) == maxDegree (G)

def components (G):
    result = []
    V = G.vertices
    while V:
	c = list (DFS (G, V[0]))
	result.append (c)
	V = [v for v in V if v not in c]
    return result

def is_connected (G):
    return len (list (DFS (G, G.vertices[0]))) == len (G.vertices)

def vertexConnectivity (G):
    return NotImplemented

def edgeConnectivity (G):
    return NotImplemented

def diameter (G):
    return NotImplemented

def radius (G):
    return NotImplemented

def chromaticNumber (G):
    return NotImplemented

def articulationVertices (G):
    return NotImplemented
