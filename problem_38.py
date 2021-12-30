def is_pandigital(n):
    """
    using all the numbers from 1 to 9

    :param n: integer n
    :return: True or False
    """
    nstr = str(n)
    if len(set(nstr)) == 9:
        if '0' not in nstr:
            return len(list(nstr)) == 9

def concat(n, m):
    """

    :param n: integer n
    :param m: number of concatenation
    :return: concatenated integer
    """
    if m == 1:
        return n

    s = str(n)
    for i in range(2, m+1):
        s += str(i*n)

    return int(s)

result = []
for i in range(9, 10000):
    for j in range(1, 6):
        num = concat(i, j)
        if is_pandigital(num):
            result.append(num)
print(max(result))