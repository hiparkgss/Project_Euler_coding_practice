import numpy as np
import time

t0 = time.time()
with open('prime_list_comma.csv', 'r') as f:
    a = f.readline().split(',')

prime_list = [int(elem) for elem in a if int(elem) < 10**6]

##########################################################
def prime_factor(prime_l, n):
    """

    Args:
        prime_l: prime list in ascending order
        n: int that is to be factorised.

    Returns:
        dict
        {prime: power}


    >>> prime_factor([2, 3, 5, 7, 11], 360)
    {2: 3, 3: 2, 5: 1}

    >>> prime_factor(prime_list, 74)
    {2: 1, 37: 1}

    >>> prime_factor(prime_list, 2738)
    {2: 1, 37: 2}

    >>> prime_factor(prime_list, 1)
    {}

    """

    d = {}
    for p in prime_l:  # for every prime

        if n == 1:
            break

        if p > np.floor(np.sqrt(n)):  # if prime is beyond the sqrt, then break
            d[n] = 1
            break

        while n % p == 0:  # if the prime is a factor
            n = n//p  # prime factor division
            try:
                d[p] += 1
            except KeyError:
                d[p] = 1

    return d

def phi(prime_l, n):
    """
    Euler phi function
    Args:
        prime_l: prime list in ascending order
        n: int input

    Returns:
        int


    >>> phi(prime_list, 36)
    12

    >>> phi(prime_list, 37)
    36

    """

    result = 1
    d = prime_factor(prime_l, n)
    for k, v in d.items():
        result = result * k ** (v-1) * (k - 1)

    return result

def nphi_ratio(prime_l, n):
    return n/phi(prime_l, n)

##########################################################

arr = np.arange(2, 10**6 + 1)
a = np.array([nphi_ratio(prime_list, elem) for elem in arr])
m = np.max(a)
max_num = arr[a == m]
print('max_num', max_num)

t1 = time.time()
print('computational time:', t1-t0)