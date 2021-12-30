import itertools as it
import numpy as np
import time

t0 = time.time()

a = np.arange(1, 10)
p = np.array(list(it.permutations(a)))  # possible permutation in row.

line1 = 10 + p[:, 0] + p[:, 1]
line2 = p[:, 5] + p[:, 1] + p[:, 2]
line3 = p[:, 6] + p[:, 2] + p[:, 3]
line4 = p[:, 7] + p[:, 3] + p[:, 4]
line5 = p[:, 8] + p[:, 4] + p[:, 0]

line_val = np.array([line2, line3, line4, line5])
bool_val = line_val == line1  # boolean of each element compared to line1


def and_applied_in_col(m):
    """
    apply and logical operation to each column
    Args:
        m (np.array): each element is boolean. matrix of size (r, c)

    Returns:
        np.array of bool: size of c
    """
    r, c = m.shape
    return np.array([np.all(m[:, i]) for i in range(c)])


candidate = and_applied_in_col(bool_val)
sol_candidate = p[candidate]


def format_magic_ring(m):
    """

    Args:
        m (np.ndarray):  matrix. each row denotes the solution

    Returns:
        format them into 16 digit.
    """
    r, c = m.shape

    ans = []
    for i in range(r):
        sol = m[i]
        clockwise = np.array([[10, sol[0], sol[1]],
                              [sol[5], sol[1], sol[2]],
                              [sol[6], sol[2], sol[3]],
                              [sol[7], sol[3], sol[4]],
                              [sol[8], sol[4], sol[0]]])

        starting_point = clockwise[:, 0]
        length = len(starting_point)
        starting_ind = np.arange(length)
        ind = np.argmin(starting_point)  # index of the starting point
        initial = np.concatenate([starting_ind[ind:], starting_ind[:ind]])
        result = clockwise[initial]

        s = ''
        for sublist in result:
            s = s + concatenate(sublist)

        ans.append(int(s))

    return ans

def concatenate(l):
    """
    Args:
        l (list or 1d array):

    Returns:
        concatenate into int
    """
    result = ''
    for s in [str(elem) for elem in l]:
        result = result + s

    return result

ans = format_magic_ring(sol_candidate)
ans = max(ans)
print(ans)
##############################################################################

t1 = time.time()
print('computational time', t1 - t0, 's')
