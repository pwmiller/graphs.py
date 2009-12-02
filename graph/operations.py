'''
This module defines functions that implement basic operations on
graphs.
'''

try:
    from itertools import product
except ImportError:
    from compatibility import product

from combinatorics import pairs

from graph import Graph, Edge

def graphPower (G, n):
    return NotImplemented

def graphCartesianProduct (G, H):
    '''
    Returns the cartesian product of graphs $G$ and $H$, defined
    as the graph having vertex set $V(G) \times V(H)$.  Vertices
    $(u_1, u_2)$ and $(v_1, v_2)$ are adjacent in the resulting
    graph if and only if either:
    \begin {enumerate}
        \item $u_1 = v_1$ and $u_2$ is adjacent to $v_2$ in $H$, or
        \item $u_2 = v_2$ and $u_1$ is adjacent to $v_1$ in $H$.
    \end{enumerate}
    '''
    vertices = list (product (G.vertices, H.vertices))
    edges = []
    for u, v in pairs (vertices):
        if u[0] == v [0] and Edge (u[1], v[1]) in H.edges:
            edges.append ( (u, v) )
        if u[1] == v[1] and Edge (u[0], v[0]) in G.edges:
            edges.append ( (u, v) )
    return Graph (vertices = vertices, edges = edges)

def graphTensorProduct (G, H):
    return NotImplemented

def graphJoin (G, H):
    return NotImplemented

def graphUnion (G, H):
    return NotImplemented

def graphIntersection (G, H):
    return NotImplemented

def graphDifference (G, H):
    return NotImplemented

def graphSum (G, H):
    return NotImplemented
