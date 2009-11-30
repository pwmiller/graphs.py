'''
This module defines functions that implement basic operations on
graphs.
'''

try:
    from itertools import product
except ImportError:
    from compatibility import product

from combinatorics import pairs

def graphPower (G, n):
    return NotImplemented

def graphCartesianProduct (G, H):
    V1 = G.vertices
    V2 = range (order (G), order (G) + order (H))
    vertices = product (V1, V2)
    
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
