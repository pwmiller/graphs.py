'''
The \code{subgraphs} module contains functions that take a graph $G$
(and possibly some other things) as input and return a subgraph of
$G$.
'''

import graph
from algorithms import DFS

def graphCenter (G):
    return NotImplemented

def vertexInducedSubgraph (G, vertices):
    vertices = set (vertices)
    edges = map (tuple, G.edges)
    edges = [ (u, v) for (u, v) in edges if set ([u, v]) <= vertices ]
    return graph.Graph (vertices = vertices, edges = edges)

def edgeInducedSubgraph (G, edges):
    vertices = []
    edges = map (tuple, edges)
    for (u, v) in edges:
        vertices.extend ( [u, v] )
    vertices = list (set (vertices))
    return graph.Graph (vertices = vertices, edges = edges)

def components (G):
    V = G.vertices
    while V:
        componentVertices = list (DFS (G, V[0]))
        yield vertexInducedSubgraph (G, componentVertices)
        V = [v for v in V if v not in componentVertices]

def nontrivialComponents (G):
    return NotImplemented
