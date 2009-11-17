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
    V = G.vertices
    while V:
        component = list (DFS (G, V[0]))
        yield component
        V = [v for v in V if v not in component]

def is_connected (G):
    return len (list (DFS (G, G.vertices[0]))) == len (G.vertices)

def is_tree (G):
    return is_connected (G) and len (G.edges) == len (G.vertices) - 1

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
