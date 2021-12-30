"""
Mathematical analysis.

Let f([p1, p2, ..., pk], n) be the number of partition of primes using prime list [p1, p2, ..., pk]
where p1 <= p2 <= ... <= pk.

Let g(n) be the function of our question.

g(10) = f([2, 3, 5, 7], 10).
g(n) = f(prime_list below n, n). Note that max(prime_list) < n.


Analysis on function f:

1. recurrence relation.
original functional value = (when the biggest prime in the prime list is not used) + (used at least once).
f([p1, ..., pk], n) = f([p1, ..., p_(k-1)], n) + f([p1, ..., pk], n - pk).

2. initial values.
f(prime_list, 0) = 1 because this means n = pk in the previous recurrence equation.
f(prime_list, n) = 0 if n < min(prime_list)
f([p1], n) = int(n % p1 == 0)


"""

import time
import numpy as np


prime_arr = np.loadtxt('prime_list_comma.csv', dtype=np.int, delimiter=',')  # prime table stored in local machine.

n_lim = 10 ** 4  # upper bound for prime_arr.
prime_arr = prime_arr[prime_arr < n_lim]
memo = {}

t0 = time.time()

#############################################################################

def f(prime_tuple, n):
    """

    Args:
        prime_tuple: tuple of prime in ascending order.
        n:

    Returns:

    """

    try:
        return memo[(prime_tuple, n)]  # the result is in dictionary
    except KeyError:
        pass


    m = prime_tuple[0]  # because prime_tuple is ascending order, m = 2
    if n == 0:
        return 1
    elif n < m:  # n can go negative as well
        return 0
    elif len(prime_tuple) == 1:
        return int(n % m == 0)
    else:
        short_prime_tuple = prime_tuple[:-1]  # discarding the last element
        result = f(short_prime_tuple, n) + f(prime_tuple, n - prime_tuple[-1])
        memo[(prime_tuple, n)] = result
        return result

def g(n):
    prime_tuple_input = tuple(prime_arr[prime_arr < n])
    return f(prime_tuple_input, n)

#############################################################################

n = 10  # initial point

while g(n) < 5001:
    n += 1

print('ans', n)

t1 = time.time()
print('computation time', (t1 - t0) * 10 ** 3, 'ms')