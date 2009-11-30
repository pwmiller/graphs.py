'''
This module implements certain functions (mostly from the itertools module)
that are present in Python 2.6 but not in 2.4.
'''


def product(*args, **kwds):
    '''
    This function replaces itertools.product when it is not available.
    '''
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def combinations(iterable, r):
    '''
    This function replaces itertools.combinations when it is not available.
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

        # pylint: disable-msg=W0631

        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
