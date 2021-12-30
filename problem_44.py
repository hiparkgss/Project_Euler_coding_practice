import itertools as it

def double_p(n):
    return n * (3 * n - 1)

def dif(l):
    """

    :param l: list given
    :return: give the absolute value of all possible pairs

    """
    n = len(l)
    return [(abs(l[elem[0]] - l[elem[1]]), min(l[elem[0]], l[elem[1]])) for elem in it.combinations(range(n), 2)]


m = 5000
pset = [double_p(n) for n in range(1, m)]
pdifset = dif(pset)
p_in = [elem for elem in pdifset if elem[0] in pset]
pf = [abs(elem[0]-elem[1]) for elem in p_in if abs(elem[0]-elem[1]) in pset]
print(pf)
print('the ans is ', pf.sort())