'''
The \code{subgraphs} module contains functions that take a graph $G$
(and possibly some other things) as input and return a subgraph of
$G$.
'''

import graph
from algorithms import DFS
from invariants import order

def graphCenter (G):
    '''
    Returns the center of $G$, defined as the graph induced by the
    subset of $V(G)$ with minimum eccentricity.
    '''
    return NotImplemented

def vertexInducedSubgraph (G, vertices):
    '''
    Return the subgraph of $G$ induced by the set \code {vertices}.
    '''
    vertices = set (vertices)
    edges = map (tuple, G.edges)
    edges = [ (u, v) for (u, v) in edges if set ([u, v]) <= vertices ]
    return graph.Graph (vertices = vertices, edges = edges)

def edgeInducedSubgraph (G, edges):
    '''
    Return the subgraph of $G$ induced by the edges in \code {edges}.
    '''
    vertices = []
    edges = map (tuple, edges)
    for (u, v) in edges:
        vertices.extend ( [u, v] )
    vertices = list (set (vertices))
    return graph.Graph (vertices = vertices, edges = edges)

def components (G):
    '''
    This is a generator that yields the components of $G$ -- that is,
    the maximal connected subgraphs.
    '''
    V = list (G.vertices)
    while V:
        componentVertices = list (DFS (G, V[0]))
        yield vertexInducedSubgraph (G, componentVertices)
        V = [v for v in V if v not in componentVertices]

def nontrivialComponents (G):
    '''
    This is a generator that yields the nontrivial components -- that
    is, the ones having more than one vertex.
    '''
    for component in components (G):
        if order (component) > 1:
            yield component
