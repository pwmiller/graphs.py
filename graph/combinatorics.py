'''
The \code{combinatorics} module implements some useful but essentially
generic combinatorical functions.
'''

try:
    from itertools import combinations
except ImportError:

    # The following is taken verbatim from the Python documentation

    def combinations(iterable, r):
        '''
        This is a drop-in replacement for itertools.combinations
        from Python 2.6.  You should only be seeing this
        if you are using a version of Python older than 2.6.
        '''
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = range(r)
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return

	    # The following comment is needed to suppress a spurious
	    # warning from pylint:

	    # pylint: disable-msg W0631
	    
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

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
    r = d = 1
    if k > n:
        return 0
    while d <= k:
        r *= n
        n -= 1
        r /= d
        d += 1
    return r
