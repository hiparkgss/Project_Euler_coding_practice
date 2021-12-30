import numpy as np
import time
import collections as coll

t0 = time.time()
with open('prime_list_comma.csv', 'r') as f:
    a = f.readline().split(',')

n_lim = 10**7

prime_list = [int(elem) for elem in a if int(elem) < n_lim]

def phi_too_long(prime_l, n):
    """
    Euler phi function
    Args:
        prime_l: prime list in ascending order
        n: int input

    Returns:
        int

    >>> phi(prime_list, 4)
    2

    >>> phi(prime_list, 36)
    12

    >>> phi(prime_list, 37)
    36

    >>> phi(prime_list, 87109)
    79180

    """
    s = set()
    num = n
    for p in prime_l:  # for every prime

        if num == 1:
            return 1

        elif num in prime_l:
            s.add(num)
            break
        elif p > np.floor(np.sqrt(num)):  # if prime is beyond the sqrt, then break
            break
        elif num % p == 0:
            num = num//p
            s.add(p)

    for p in s:
        n = n - n//p

    return n

def dic_phi(prime_l, nlim):
    """

    Args:
        prime_l: prime list
        nlim: int limit

    Returns:
         dict
         {n: np.array of prime numbers equal or less than n}


    """
    col = np.arange(2, nlim)
    row = np.array(prime_l)
    d1 = {prime: np.arange(prime, nlim, prime) for prime in prime_l}  # prime: np.array of prime multiple.
    phi_arr = np.arange(2, nlim)
    for k, v in d1.items():
        phi_arr[v-2] = phi_arr[v-2]//k * (k-1)


    return phi_arr, row, col

def phi(d, row, col):
    """

    Args:
        d:
        row:
        col:

    Returns:
        np.array of phi value of col.
        euler_phi(col).

    """
    result = []
    for k in col:
        n = k
        divisible_prime_arr = d[k]
        numerator = np.prod(divisible_prime_arr - 1)
        denominator = np.prod(divisible_prime_arr)
        n = n//denominator
        n = n * numerator
        result.append(n)

    return np.array(result)



def is_permutation(arg1, arg2):
    """

    Examples:
        >>> is_permutation(12345, 54321)
        True

        >>> is_permutation(12345, 5321)
        False

        >>> is_permutation(123333345, 543333321)
        True



    """

    arg3 = sorted(str(arg1))
    arg4 = sorted(str(arg2))

    return arg3 == arg4


phi_arr, row, col = dic_phi(prime_list, n_lim)
num_ele = len(col)
# permutation_bool_arr = np.array([is_permutation(col[i], phi_arr[i]) for i in range(num_ele)])
permutation_bool_arr = np.array(list(map(is_permutation, col, phi_arr)))
n_phi_ratio = col/phi_arr
min_val = np.min(n_phi_ratio[permutation_bool_arr])
ans = col[n_phi_ratio == min_val]
print('ans', ans)
print('min_val', min_val)

t1 = time.time()
print('computational time:', t1-t0)