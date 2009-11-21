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

def PetersenGraph ():
    return generalizedPetersenGraph (5, 2)

def generalizedPetersenGraph (n, k):
    if n < 2 or k < 1 or k > floor ( (n-1) / 2 ):
        raise ValueError, "Parameters out of range."

def completeGraph (*ns):
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
