import itertools as it
import numpy as np
import networkx as nx
import collections as col
import time

t0 = time.time()

#####################################################################################
def count_digits(l):
    """

    Args:
        l: list of integer.
        same digit list.

    Returns:
        dict
        sorted list [ counter results in tuple]: {relevant ints in set}

    """
    num = len(l)
    l1 = [tuple(sorted(list(col.Counter(str(elem)).items()))) for elem in l]
    d1 = {}

    for i in range(num):
        try:
            d1[l1[i]].add(l[i])
        except KeyError:
            d1[l1[i]] = {l[i]}

    return d1.values()
#####################################################################################

nlim = 10**4

a = np.arange(1, nlim)
a3 = a ** 3
log_a3 = np.log10(a3)
digit_number = np.ceil(log_a3)
digit_number = digit_number.astype('int64')

largest_digit = digit_number[-1]

# now collect the same digit numbers together
for d in range(largest_digit+1):
    print('\n\ndigit is', d)
    same_digit_arr = a3[digit_number == d]
    d_values = count_digits(same_digit_arr)

    g = nx.Graph()
    for set_d in d_values:
        set_of_tu = set(it.combinations(set_d, 2))
        g.add_edges_from(set_of_tu)

    print('trying cliques')
    ans = nx.find_cliques(g)
    ans = [sublist for sublist in ans if len(sublist) > 4]
    if ans:
        print('5 cubed numbers are', ans)


t1 = time.time()
print('Computation time:', t1-t0)