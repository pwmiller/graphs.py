'''
The \code{graph} module implements the graph data structure itself,
as well as functions for converting graph structures to and from
the adjacency list and adjacency matrix representations.
'''

import sympy

class Edge (object):
    '''
    This object implements a generic graph edge.  If \code {e} is an
    \code {Edge} object, then \code {e[0]} and \code {e[1]} are the
    vertices incident with \code {e}.

    If the keyword argument \code {directed = True} is passed to
    \code {__init__}, then the instance constructed represents the
    directed edge from \code {e[0]} to \code {e[1]}.  Otherwise, it
    represents an undirected edge.
    '''
    def __init__(self, *args, **kwargs):
        if len (args) != 2:
            raise TypeError ("An edge must contain exactly two vertices.")
        self.__data = (args[0], args[1])
        if 'directed' in kwargs:
            self.directed = kwargs ['directed']
        else:
            self.directed = False

    def __getitem__(self, key):
        if key == 0 or key == 1:
            return self.__data[key]
        elif not isinstance (key, int):
            raise TypeError ("Valid indices are 0 or 1")
        else:
            raise IndexError ("Valid indices are 0 or 1")

    def __len__(self):
        return len (self.__data)

    def __str__(self):
        return "(%(v1)s%(directed)s%(v2)s)" % \
               { 'v1' : self [0],
                 'v2' : self [1],
                 'directed': [', ', '->'] [int (self.directed)] }

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance (other, self.__class__):
            if self.directed:
                return self.__data == (other[0], other[1])
            else:
                return sorted (list (self.__data)) == \
                       sorted (list ( (other[0], other[1])))
        else:
            return False

class Graph (object):
    '''
    This object implements the mathematical definition of a graph.  That
    is, a graph $G = (V, E)$ consists of a finite set $V$, called the
    \emph {vertex set} of $G$, and a set $E$ (called the \emph {edge set}
    of $G$) of pairs of distinct vertices from $V$
    '''
    def __init__(self, vertices = None, edges = None, directed = False):
        if vertices is None:
            vertices = []
        if edges is None:
            edges = []

        self.vertices = list (set (vertices))

        for e in edges:
            if e[0] not in self.vertices or \
               e[1] not in self.vertices or \
               len (e) != 2:
                raise TypeError ("%(edge)s is not a valid edge." \
                                 % { 'edge' : e } )

        self.edges = [ Edge (e[0], e[1], directed = directed) for e in edges ]

def fromAdjacencyMatrix (M):
    '''
    Constructs a graph $G$ from the matrix $M$.  If $M$ is symmetric, we
    assume the graph $G$ returned is undirected, otherwise $G$ is directed.
    '''
    M = sympy.matrices.Matrix (M)
    if M != M.transpose():
        directed = True
    else:
        directed = False
    n = M.shape[0]
    vertices = range (n)
    edges = [ (x, y) for x in range (n) for y in range (n) if M[x, y] != 0]
    return Graph (vertices = vertices, edges = edges, directed = directed)

def adjacencyMatrix (G):
    '''
    Returns the adjacency matrix of the graph $G$.
    '''
    n = len (G.vertices)
    M = sympy.matrices.zeros (n)
    for edge in G.edges:
        i = G.vertices.index (edge[0])
        j = G.vertices.index (edge[1])
        M[i, j] = 1
        if not edge.directed:
            M[j, i] = 1
    return M

def incidenceMatrix (G):
    '''
    Returns the incidence matrix $B$ of the graph $G$.  If $G$ has order $n$
    and size $m$, then $B$ is the $n \times m$ matrix where $b_{ij}$ is $1$
    if the vertex $v_i$ and the edge $e_j$ are incident, otherwise $0$.
    '''
    n = len (G.vertices)
    m = len (G.edges)

    def b(i, j):
        return G.vertices [i] in G.edges [j]

    return sympy.matrices.Matrix (n, m, b)

def fromAdjacencyLists (Ls):
    '''
    Constructs a graph $G$ from a the sequence of two-element sequences
    of the form \code { (v, (u_1, u_2, ... u_k) )}, indicating that the
    vertex $v$ is adjacent to each of $u_1, u_2, \dots, u_k$.
    '''
    Ls = dict (Ls)
    vertices = []
    edges = []
    for v, neighbors in Ls:
        vertices.append (v)
        for u in neighbors:
            edges.append ( (u, v) )
    return Graph (vertices = vertices, edges = edges)

def adjacencyLists (G):
    '''
    Returns the dict \code {adjacencies}, where
    \code {adjacencies.keys()} == list (G.vertices) and for
    each \code {v} in \code {G.vertices}, we have that
    \code {adjacencies [v]} is a list of all the vertices adjacent
    to \code {v} in the graph $G$.
    '''
    adjacencies = {}
    for v in G.vertices:
        adjacencies [v] = []
        for edge in [e for e in G.edges if v in e]:
            if edge.directed:
                if edge[0] == v:
                    adjacencies[v].append (edge[1])
            else:
                u = [x for x in edge if x != v] [0]
                adjacencies[v].append (u)

    return adjacencies

def dotString (G):
    '''
    Returns a string suitable for passing to the \code {dot} program from
    the \code {graphviz} graph drawing toolkit.
    '''
    return NotImplemented
