"""
Mathematical analysis

given the continued fraction list: [a0, ..., a_n]. n+1 elements

The basic formula is A + B/C.

Let's start from the bottom.
a(n-1) + 1/a(n)  = A1 + B1/C1 where A1 = a(n-1), B1 = 1, C1 = a(n)

Recurrence relation gives
A2 = a(n-2), B2 = C1, C2 = A1*C1 + B1

Final answer is An + Bn/Cn = (An * Cn + Bn)/Cn

"""

import time
import numpy as np

t0 = time.time()

nlim = 100
arr = np.ones(nlim).astype(np.int)

# third element is 2k
arr[2::3] = 2 * np.arange(1, len(arr[2::3]) + 1)

# the first element is 2
arr[0] = 2


def simplify_continued_fraction(nparr):
    """

    Args:
        nparr: numpy array

    Returns:
        tuple of int
        (numerator, denominator)

    """
    n = len(nparr) - 1

    # python int is not restricted by the integer size as for np.int64
    a = nparr[n-1].item()
    b = 1
    c = nparr[n].item()

    for i in range(n - 1):
        b, c = c, a * c + b
        a = nparr[n - 2 - i].item()

    return a * c + b, c

def digit_sum(n):
    """

    Args:
        n: int

    Returns:
        int
        sum of digit

    """
    return sum(int(elem) for elem in list(str(n)))


n, d = simplify_continued_fraction(arr)
ans = digit_sum(n)

print('ans', ans)
t1 = time.time()
print('computation time', (t1 - t0) * 10**3, 'ms')
