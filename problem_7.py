def find_prime(n):
    """
    :param n: (int) input number
    :return: (list) a list of prime numbers below n

    >>> find_prime(10)
    [2, 3, 5, 7]

    >>> find_prime(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    prime = []
    all_num = list(range(2, n + 1))
    while True:
        prime.append(all_num.pop(0))
        all_num = list(filter(lambda x: x % prime[-1] != 0, all_num))
        if all_num == []:
            break

    return prime

print(find_prime(111000)[10000])