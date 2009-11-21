'''
A \emph {graph invariant} is a function that will return the same value when
passed different, but isomorphic graphs as parameters.  This module implements
several common graph invariants.
'''

import graph
from algorithms import DFS
from combinatorics import binomial
from math import floor

def order (G):
    '''
    Returns the order (\textit{i.e.}\ the number of vertices) of the
    graph $G$.
    '''
    return len (G.vertices)

def size (G):
    '''
    Returns the size (number of edges of) the graph $G$.
    '''
    return len (G.edges)

def degrees (G):
    '''
    Returns a generator object that yields the degree of each vertex
    of $G$, in no particular order.
    '''
    return (len ([e for e in G.edges if v in e]) for v in G.vertices)

def degreeSequence (G):
    '''
    Returns the list of vertex degrees of $G$ in nonincreasing order.
    '''
    return reversed (sorted (degrees (G)))

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

def is_connected (G):
    '''
    Returns True if and only if $G$ is connected, otherwise returns False.
    '''

    delta = minDegree (G)
    n = order (G)

    # By Theorem 1.3.15 of West, if $G$ is a simple, $n$-vertex graph with
    # minDegree (G) >= (n-1)/2, then $G$ is connected.

    if delta >= (n - 1) / 2:
        return True
    else:
        return len (list(DFS (G))) == len (G.vertices)

def is_tree (G):
    '''
    Returns True if and only if $G$ is a tree, otherwise returns False.
    '''
    return is_connected (G) and len (G.edges) == len (G.vertices) - 1

def is_bipartite (G):
    return NotImplemented

def is_triangleFree (G):
    '''
    Returns True if $G$ is triangle-free, otherwise False.
    '''
    # By Mantel's Theorem (West, p. 41), the maximum number of edges in
    # an $n$-vertex triangle-free simple graph is the floor of $n^2 / 4$.

    n = order (G)
    if size (G) > floor (n**2 / 4.0):
        return False

    # Otherwise, recall that the $(i,j)$ entry of the $n$-th power of the
    # adjacency matrix of a graph indicates the number of closed walks
    # that begin at $v_i$ and end at $v_j$. (West, p. 455, Proposition
    # 8.6.7.)

    # A triangle is a closed walk of length $3$ starting and ending at
    # the same vertex.  Thus, we see that $G$ is triangle-free if and
    # only if $\trace (A^3) = 0$, where $A$ is the adjacency matrix of $G$.

    A = graph.toAdjacencyMatrix (G)
    return (A**3).trace() == 0

def is_complete (G):
    '''
    Returns True if $G$ is a complete graph, otherwise False.
    '''
    return size (G) == binomial (order (G), 2)

def eigenvalues (G):
    '''
    Returns the eigenvalues of the adjacency matrix of $G$.
    '''
    return graph.toAdjacencyMatrix(G).eigenvals()

def laplacianEigenvalues (G):
    return NotImplemented

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

def is_eulerian (G):
    return NotImplemented

def is_hamiltonian (G):
    return NotImplemented

def is_selfComplementary (G):
    '''
    See West, p. 17., exercise 1.1.31.
    '''
    return NotImplemented

def girth (G):
    return NotImplemented
