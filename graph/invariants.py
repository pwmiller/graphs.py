'''
A \emph {graph invariant} is a function that will return the same value when
passed different, but isomorphic graphs as parameters.  This module implements
several common graph invariants.
'''

from algorithms import DFS

def degrees (G):
    '''
    Returns the degree of each vertex of $G$, in no particular order.
    '''
    return set ([len ([e for e in G.edges if v in e]) for v in G.vertices])

def degreeSequence (G):
    return sorted (list (degrees (G)))

def minDegree (G):
    '''
    Returns the smallest degree of any vertex in the vertex set of $G$.
    '''
    return min (degrees (G))

def maxDegree (G):
    '''
    Returns the largest degree of any vertex in the vertex set of $G$.
    '''
    return max (degrees (G))

def is_regular (G):
    '''
    Returns True if and only if every vertex of $G$ has the same degree,
    otherwise returns False.
    '''
    return minDegree (G) == maxDegree (G)

def components (G):
    V = G.vertices
    while V:
        component = list (DFS (G, V[0]))
        yield component
        V = [v for v in V if v not in component]

def is_connected (G):
    '''
    Returns True if and only if $G$ is connected, otherwise returns False.
    '''
    return len (list (DFS (G, G.vertices[0]))) == len (G.vertices)

def is_tree (G):
    '''
    Returns True if and only if $G$ is a tree, otherwise returns False.
    '''
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
