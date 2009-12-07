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
from math import floor
try:
    from itertools import product
except ImportError:
    from compatibility import product
from operations import graphCartesianProduct

def generalizedPetersenGraph (n, k):
    '''
    The \emph {generalized Petersen graph} is the graph with vertex
    set $\{u_0, u_1, \dots, u_{n-1}, v_0, v_1, \dots, v_{n-1}\}$ and
    edge set $\{u_i u_{i+1}, u_i v_i, v_i v_{i+k}: 0 \leq i \leq n-1\}$,
    where the subscripts are taken modulo $n$.
    '''
    if n < 2 or k < 1 or k > floor ( (n-1) / 2 ):
        raise ValueError ("Parameters out of range.")
    u = range (n)
    v = range (n, 2 * n)
    vertices = u + v
    edges = []
    for i in range (n):
        edges.append ( (v[i], v[(i+1) % n]) )
        edges.append ( (v[i], u[i]) )
        edges.append ( (u[i], u[(i+k) % n]) )
    return graph.Graph (vertices = vertices, edges = edges)

def PetersenGraph ():
    '''
    Returns the infamous Petersen graph.
    '''
    return generalizedPetersenGraph (5, 2)

def oddGraph (k):
    ''' See West, p. 17. for definition '''
    return NotImplemented

def completeGraph (*ns):
    '''
    Returns the complete graph $K_{n_1, n_2, \dots, n_k}$ when passed
    the sequence \code {n_1, n_2, \dots, n_k}.
    '''

    # The folowing is to silence a spurious pylint warning:
    # pylint: disable-msg=W0142

    if len (ns) == 1:
        if ns[0] == 1:
            return graph.Graph (vertices = [1], edges = [])
        else:
            return completeGraph ( * ([1] * ns[0]) )

    n = sum(ns)
    vertices = range (n)
    edges = []
    for group in xrange(len(ns)):
        lo = sum(ns[:group-1])
        hi = sum(ns[:group])
        edges.extend((i, j) for (i, j) in product (
            xrange(lo, hi), xrange(hi, n)))

    return graph.Graph (vertices = vertices, edges = edges)

def path (n):
    '''
    Returns the path graph on $n$ vertices.
    '''
    vertices = range (n)
    edges = [ (i, i+1) for i in range (n-1) ]
    return graph.Graph (vertices = vertices, edges = edges)

def hypercube (k):
    '''
    Returns the $k$-dimensional hypercube graph.  See West, p. 36,
    example 1.3.8.
    '''
    G = completeGraph (1)
    P2 = completeGraph (2)
    while k:
        G = graphCartesianProduct (G, P2)
        k -= 1
    return G

def tetrahedron():
    '''
    Returns the graph of the tetrahedron.
    '''
    return completeGraph (4)

def cube():
    '''
    Returns the graph of the cube.
    '''
    return hypercube (3)

def octahedron():
    '''
    Returns the graph of the octahedron.
    '''
    return completeGraph (2, 2, 2)

def dodecahedron():
    '''
    Returns the graph of the dodecahedron.
    According to
    http://mathworld.wolfram.com/GeneralizedPetersenGraph.html,
    this is the same as generalizedPetersenGraph (10,2)
    '''
    return generalizedPetersenGraph (10, 2)

def icosahedron():
    '''
    Returns the graph of the icosahedron.
    '''
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

def gridGraph (m, n):
    return graphCartesianProduct (path (m), path (n))

# The following are listed on p. 12 of West as "The Graph Menagerie."
# The menagierie is a set of graphs on $5$ or fewer vertices that
# come up frequently enough in graph theory that they have names.

def triangle():
    '''
    Returns the triangle graph, $K_3$.
    '''
    return completeGraph(3)

def claw():
    '''
    Returns the claw graph, $K_{1,3}$.
    '''
    return completeGraph (1, 3)

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
