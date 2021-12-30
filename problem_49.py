with open('prime_list_comma.csv', 'r') as f:
    prime_overall_list = f.readline().split(',')

def permu(n):
    """

    :param n: integer
    :return: dictionary of digit count
    """
    a = {}
    s = str(n)
    for char in s:
        if char in a:
            a[char] += 1
        else:
            a[char] = 1
    return a

def is_permu(m, n):
    """

    :param n: list of 4 digit integer
    :return: True of False
    """
    return permu(m) == permu(n)


prime = [int(elem) for elem in prime_overall_list if 1000 < int(elem) < 10000]
pset = set(prime)
n = len(prime)
for i in range(n):
    for j in range(i+1, n):
        if is_permu(prime[i], prime[j]):
            new = 2 * prime[j] - prime[i]
            if new in pset:
                if is_permu(new, prime[i]):
                    print(str(prime[i]) + str(prime[j]) + str(2 * prime[j] - prime[i]))