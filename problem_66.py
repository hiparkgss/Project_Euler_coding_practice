import time
import numpy as np
import fractions as frac

n_lim = 10 ** 3  # upper bound for prime_arr.


t0 = time.time()

# possible D values
arr = np.arange(2, n_lim + 1)
sqrt_arr = np.sqrt(arr)
sqrt_int_arr = np.floor(sqrt_arr)

arr = arr[sqrt_arr != sqrt_int_arr]  # remove the square integer

def get_continued_fraction(d, n):
    """
    Args:
        d (int): parameter d of Pell's equation
        n (int): number for the index of the last sequence a_n.

    Returns:
        list of int: Continued fraction [a0, a1, a2, ... a_n] of sqrt(d)

    A/B + C/D sqrt(d) form.

    """
    # initialisation
    result = []
    A = 0
    B = 1
    C = 1
    D = 1
    sqrt = np.sqrt(d)

    # setting up the equation
    f1 = frac.Fraction(A, B)
    f2 = frac.Fraction(C, D)
    eq = f1 + f2 * sqrt
    a = int(eq)
    result.append(a)  # initialise with a0

    for i in range(n):

        # update on A, B, C
        A1 = B * D**2 * (A - B * a)
        B1 = D**2 * (A - B * a)**2 - B**2 * C**2 * d
        C1 = - B**2 * C * D
        D1 = B1

        # change of variables
        A = A1
        B = B1
        C = C1
        D = D1

        # setting up the equation
        f1 = frac.Fraction(A, B)
        f2 = frac.Fraction(C, D)
        eq = f1 + f2 * sqrt
        a = int(eq)
        result.append(a)

        # simplify A, B, C for the next iteration to irreducible fraction
        A = f1.numerator
        B = f1.denominator
        C = f2.numerator
        D = f2.denominator


    return result

def convergents(d, n):
    """
    convergent of sqrt(d) is returned.

    Args:
        d (int):
        n (int): length of the list

    Returns:
        list of convergents. [(p1, q1), (p2, q2), ..., (pn, qn)]
    """
    cf = get_continued_fraction(d, n)
    # list p and q indexing starts from -1.
    # p = [p_{-1}, p0, p1, ...]
    p = [1, cf[0]]
    q = [0, 1]

    for i in range(1, n+1):
        next_p = cf[i] * p[i] + p[i-1]
        next_q = cf[i] * q[i] + q[i - 1]
        p.append(next_p)
        q.append(next_q)

    result = list(zip(p, q))
    return result[2:]


def solve(d, n):
    """

    Args:
        d (int): d parameter in Pell's eq
        n (int): using up to 'n' th convergent

    Returns:
        tuple of int. minimal solution (x, y)
    """
    candidate = np.array(convergents(d, n))
    pell = candidate[candidate[:, 0] ** 2 - d * candidate[:, 1] ** 2 == 1][:, 0]

    try:
        return np.min(pell)
    except ValueError:
        # no such candidate exists. zero size pell input to np.min
        n = 2 * n
        solve(d, n)

#################################################

# now finding for arr

n_convergent = 100

minimal_x = np.array([solve(i, n_convergent) for i in arr])
m = np.max(minimal_x)
ans = arr[minimal_x == m]

print(ans)

###############################################################
t1 = time.time()
print('computational time', t1 - t0, 's')