def realizeDegreeSequence (d):
    return NotImplemented

def DFS (G, v):

    def neighbors (v):
        return [ list (set (e).symmetric_difference (set ([v])))[0] for e in G.edges if v in e]

    yield v
    visited = set ([v])
    S = []
    for vertex in neighbors (v):
        S.append (vertex)
    while len (S):
        w = S.pop()
        for u in neighbors (w):
            if u not in visited:
                yield u
                visited.add (u)
                S.append (u)

def BFS (G, v):
    return NotImplemented

def Prim (G, weights):
    return NotImplemented

import heapq

def Kruskal (G):
    subsets = [set ([v]) for v in G.vertices]
    heap = [ (G.weight (e), e) for e in G.edges ]
    heapq.heapify (heap)
    T = set ([])
    n = len (G.vertices)
    while len (T) < n-1:
        (w, e) = heapq.heappop (heap)
        (u, v) = e
        contains_u = None
        contains_v = None
        for s in subsets:
            if u in s:
                contains_u = s
            if v in s:
                contains_v = s
            if contains_u is not None and contains_v is not None:
                break
        if contains_u != contains_v:
            T.add ((u,v))
            contains_u = contains_u.union (contains_v)
            contains_v = contains_v.union (contains_u)
    return T
