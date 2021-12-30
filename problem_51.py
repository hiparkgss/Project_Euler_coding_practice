import sys

with open('prime_list_comma.csv', 'r') as f:
    overall_list_string = f.readline().split(',')

small = 56002  # the ans is bigger than this

prime_list = [int(elem) for elem in overall_list_string if 1000000 > int(elem) > small]
prime_set = set(prime_list)


def is_triple(n):
    """

    :param n: integer n
    :return: True if it has three same digit

    """
    d = {}
    s = str(n)
    result = []
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for k, v in d.items():
        if v == 3:
            result.append(int(k))


    m = len(result)
    if m == 0:
        return False,
    else:
        result.sort()
        return True, result


def index(l, m):
    """

    :param l: list
    :param m: an element in the list l
    :return: index of m (could be multiple)

    """
    if m not in l:
        raise ValueError('second argument is not in the first argument number')

    return [i for i, j in enumerate(l) if j == m]


def list_to_int(l):
    """

    :param l: list with single digit integer
    :return: make a integer with list
    """
    for elem in l:
        if not len(str(elem)) == 1:
            raise ValueError('not a single digit element list')
        elif not type(elem) == int:
            raise ValueError('a single digit element is not integer type')

    l1 = reversed(l)
    return sum(10 ** i * j for i, j in enumerate(l1))


def change_digit(n, m):
    """

    :param n: integer number input
    :param m: a 1-digit number that is going to be changed
    :return: possible numbers

    """
    result = []
    l = [int(elem) for elem in list(str(n))]
    if m not in l:
        raise ValueError('second argument is not in the first argument number')
    il = index(l, m)

    for j in range(10):
        for ind in il:
            l[ind] = j
        result.append(list_to_int(l))

    return result


triple_prime_list = [(prime, is_triple(prime)[1]) for prime in prime_list if is_triple(prime)[0]]

for prime in triple_prime_list:
    for elem in prime[1]:
        count = 0
        for e in change_digit(prime[0], elem):
            if e in prime_set:
                count += 1
        if count == 8:
            print(prime[0])
            sys.exit()
