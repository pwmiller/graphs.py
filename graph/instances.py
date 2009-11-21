'''
The \code{instances} module provides two broad classes of entity:
\begin{enumerate}
    \item Functions which construct individual instances of a
    parameterized family of graphs, and

    \item Individual instances of graphs that are not members of a
    parameterized family, but are nonetheless interesting or useful.
\end{enumerate}
'''

import graph
from combinatorics import pairs
from math import floor

def generalizedPetersenGraph (n, k):
    if n < 2 or k < 1 or k > floor ( (n-1) / 2 ):
        raise ValueError, "Parameters out of range."

def PetersenGraph ():
    return generalizedPetersenGraph (5, 2)

def oddGraph (k):
    ''' See West, p. 17. for definition '''
    return NotImplemented

def K (*ns):
    '''
    Returns the complete graph $K_{n_1, n_2, \dots, n_k}$ when passed
    the sequence \code {n_1, n_2, \dots, n_k}.
    '''
    return NotImplemented

def hypercube (k):
    '''
    Returns the $k$-dimensional hypercube graph.
    '''
    return NotImplemented

def tetrahedron():
    return graph.Graph (vertices = range (4), edges = pairs (range (4)))

def cube():
    return graph.fromAdjacencyMatrix (
        ([0, 1, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 1],
         [0, 1, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 0, 1],
         [0, 0, 0, 1, 1, 0, 1, 0])   )

def octahedron():
    return graph.fromAdjacencyMatrix (
        ( [0, 1, 1, 1, 0, 1],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 0, 1, 1],
          [1, 1, 0, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [1, 0, 1, 1, 1, 0] )       )

def dodecahedron():
    return graph.fromAdjacencyMatrix (
        ([0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]))

def icosahedron():
    return graph.fromAdjacencyMatrix (
        ( [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
          [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
          [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
          [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0] ) )

# The following are listed on p. 12 of West as "The Graph Menagerie."
# The menagierie is a set of graphs on $5$ or fewer vertices that
# come up frequently enough in graph theory that they have names.

def triangle():
    return K(3)

def claw():
    return NotImplemented

def paw():
    return NotImplemented

def kite():
    return NotImplemented

def house():
    return NotImplemented

def bull():
    return NotImplemented

def bowtie():
    return NotImplemented

def dart():
    return NotImplemented
