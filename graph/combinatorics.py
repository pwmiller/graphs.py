'''
The \code{combinatorics} module implements some useful but essentially
generic combinatorical functions.
'''

try:
    from itertools import combinations
except ImportError:
    from compatibility import combinations

def pairs (seq):
    '''
    Returns a generator that successively yields all pairs of distinct
    elements of the sequence \code{seq}.
    '''
    return combinations (seq, 2)

def binomial (n, k):
    '''
    Calculates the binomial coefficient ${n \choose k}$.
    '''
    if k > n / 2:
        return binomial (n, n-k)
    if k < 0:
        return 0
    r = d = 1
    if k > n:
        return 0
    while d <= k:
        r *= n
        n -= 1
        r /= d
        d += 1
    return r
