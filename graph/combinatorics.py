try:
    from itertools import combinations
except ImportError:

    # The following is taken verbatim from the Python documentation

    def combinations(iterable, r):
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
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def pairs (seq):
    return combinations (seq, 2)

def binomial (n, k):
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
