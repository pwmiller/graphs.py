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
