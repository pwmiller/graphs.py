import itertools

def pairs (seq):
    return itertools.combinations (seq, 2)

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
