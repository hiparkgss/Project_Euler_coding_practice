def factor_or(a, b, c):
    """(int, int, int) -> int

    sum all the integers that are multiple of b and c but less than a

    >>> factor_or(10, 3, 5)
    23
    """
    b_multiple = set(range(b, a, b))
    c_multiple = set(range(c, a, c))
    total_set = b_multiple.union(c_multiple)
    return sum(num for num in total_set)

print(factor_or(1000, 3, 5))
