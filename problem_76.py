"""
Mathematical analysis

One can find recurrence relation.
Define f(n) to be the number of ways of sum.
e.g. f(5) = 6 as given in the example

Define g(n, r) be the number of ways to write sum in the following format:
x1 + x2 + ... + xn = r
where x1 >= x2 >= ... >= xn >= 1

f(5) = g(2, 5) + g(3, 5) + g(4, 5) + g(5, 5)

g(2, 5) = 2
g(3, 5) = 2
g(4, 5) = 1
g(5, 5) = 1


For a given integer r, g(r-1, r) = 1 because (x1, x2, ..., xn) =  (2, 1, 1, ..., 1)
and g(r, r) = 1 because (x1, x2, ..., xn) =  (1, 1, 1, ..., 1).

g(2, r) = int(r/2) from observation.

g(3, r) = g(2, r - 1) + g(2, r - 4) + g(2, r - 7) + ...
g(4, r) = g(3, r - 1) + g(3, r - 5) + g(3, r - 9) + ...

g(n, r) = g(n - 1, r - 1) + g(n - 1, r - 1 - 1*n) + g(n - 1, r - 1 - 2*n) + ...

###################################################### found from thread.
or simply
g(n, r) = g(n - 1, r - 1) + g(n, r - n)

"""

import numpy as np
import time

t0 = time.time()

d = {}

################################################
def g(n, r):
    """

    Args:
        n:
        r:

    Returns:

    Examples:
        >>> g(2, 5)
        2
        >>> g(3, 5)
        2
        >>> g(4, 5)
        1
        >>> g(5, 5)
        1
        >>> g(3, 10)
        8


    """

    try:
        val = d[(n, r)]
        return val
    except KeyError:
        pass

    if n > r:
        return 0
    elif n == 1:
        return 0
    elif r < 2:
        return 0
    elif n == r:
        d[(n, r)] = 1
        return 1
    elif n + 1 == r:
        d[(n, r)] = 1
        return 1
    elif n == 2:
        d[(n, r)] = int(r/2)
        return int(r/2)
    else:
        r_arr = r - np.arange(1, r, n)
        n_arr = np.ones(len(r_arr), dtype=np.int) * (n - 1)
        result = np.sum(list(map(g, n_arr, r_arr)))
        d[(n, r)] = result
        return result

def f(n):
    n_arr = np.arange(2, n+1)
    r_arr = np.ones(len(n_arr), dtype=np.int) * n
    return np.sum(list(map(g, n_arr, r_arr)))


################################################
a = f(100)
print('ans', a)
t1 = time.time()
print('computation time:', t1 - t0)
