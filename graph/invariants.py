'''
A \emph {graph invariant} is a function that will return the same value when
passed different, but isomorphic graphs as parameters.  This module implements
several common graph invariants.
'''

# pylint complains about 'from graph import *', but we know what we're doing,
# so we'll suppress the warning.  The following comment tells pylint to STFU
# about it:

# pylint: disable-msg=W0401

from graph import *
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

    def degree (v):
        '''
        Returns the degree of a single vertex $v$ from our graph $G$.
        '''
        return len ([e for e in G.edges if v in e])

    return (degree (v) for v in G.vertices)

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
    '''
    Returns True if $G$ is bipartite, otherwise returns False.
    '''
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
    # of length $n$ that begin at $v_i$ and end at $v_j$. (West, p. 455,
    # Proposition 8.6.7.)

    # A triangle is a closed walk of length $3$ starting and ending at
    # the same vertex.  Thus, we see that $G$ is triangle-free if and
    # only if $\trace (A^3) = 0$, where $A$ is the adjacency matrix of $G$.

    A = toAdjacencyMatrix (G)
    return (A**3).trace() == 0

def numberOfTriangles (G):
    '''
    Returns the number of triangles in $G$ by using the fact that the $(i,i)$
    entry of the cube of the adjacency matrix of $G$ indicates the number of
    closed walks of length $3$ that start and end at vertex $v_i$
    (\textit {i.e.\} the number of triangles that $v_i$ participates in).  To
    get the total number of triangles in the whole graph, we must note that if
    three vertices $v_1, v_2, v_3$ form a triangle, the trace counts this
    six times.  So, we correct for this by dividing by $6$.
    '''

    A = toAdjacencyMatrix (G)
    return (A**3).trace() / 6

def is_complete (G):
    '''
    Returns True if $G$ is a complete graph, otherwise False.
    '''
    return size (G) == binomial (order (G), 2)

def is_empty (G):
    '''
    Returns True if $G$ is an empty graph, otherwise False.
    '''
    return size (G) == 0

def eigenvalues (G):
    '''
    Returns the eigenvalues of the adjacency matrix of $G$.
    '''
    eigenvals = toAdjacencyMatrix(G).eigenvals()

    # The following is necessary because the dictionary returned by
    # \code{sympy.Matrix.eigenvals()} uses \code{sympy.Integer}s as
    # keys rather than ordinary integers.  Thus, we get the annoying
    # situation where (for example), eigenvals() might return the
    # dict \code{\{4: 1, -2: 2, 0: 3\}}, but the expression
    # \code {4 in eigenvals} would fail.

    return dict ( [ (int (k), eigenvals [k]) for k in eigenvals.keys() ] )

def laplacianEigenvalues (G):
    '''
    Returns the eigenvalues of the Laplacian matrix of $G$.
    '''
    return NotImplemented

def vertexConnectivity (G):
    '''
    Returns the vertex connectivity of $G$ -- the minimum number of vertices
    we have to remove from $G$ to disconnect the graph.
    '''
    return NotImplemented

def edgeConnectivity (G):
    '''
    Returns the edge connectivity of $G$ -- the minimum number of edges
    we have to remove from $G$ to disconnect the graph.
    '''
    return NotImplemented

def diameter (G):
    '''
    Returns the diameter of $G$, which is defined as the maximum distance
    separating any pair of vertices in $G$.
    '''
    return NotImplemented

def radius (G):
    '''
    Returns the radius of $G$, defined as the minimum eccentricity over all
    vertices in \code {G.vertices}.
    '''

    return NotImplemented

def chromaticNumber (G):
    '''
    Returns the chromatic number of $G$, the minimum number of colors needed
    to color the vertices of $G$ such that no two vertices with the same
    color are adjacent.
    '''
    return NotImplemented

def is_eulerian (G):
    '''
    Returns True if there is a walk in $G$ that covers each edge exactly once,
    otherwise returns False.
    '''
    return NotImplemented

def is_hamiltonian (G):
    '''
    Returns True if $G$ has a hamiltonian (spanning) cycle, otherwise returns False.
    '''
    return NotImplemented

def is_selfComplementary (G):
    '''
    See West, p. 17., exercise 1.1.31.
    '''
    return NotImplemented

def girth (G):
    '''
    Returns the girth of $G$ \textit {i.e.\} the length of a shortest
    cycle in $G$.
    '''
    return NotImplemented
