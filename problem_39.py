import math as m

def is_square(n):
    """

    :param n: integer n
    :return: True or False
    """
    return int(m.sqrt(n)) ** 2 - n == 0

l = []
for i in range(1, 1000):
    for j in range(i, 1000):
        p_sq = i**2 + j**2
        if is_square(p_sq):
            if p_sq <= 10 ** 6:
                 l.append((i, j, int(m.sqrt(p_sq))))

d = {}
for tu in l:
    s = sum(tu)
    if s <=1000:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1

mk = max(d.values())
print('maximum value is', mk)
print('test case', d[120])
print([key for key in d.keys() if d[key] == mk])