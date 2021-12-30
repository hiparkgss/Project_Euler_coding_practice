#  from problem_3
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

from functools import reduce

def smallest(n):
    prime_list = find_prime(n)
    prime_factor_list = []

    for prime in prime_list:
        i = 1

        while prime ** i <= n:
            i += 1
        prime_factor_list.append(i-1)

    if len(prime_list) != len(prime_factor_list):
        print('dimension is inconsistent')

    l = [prime_list[i] ** prime_factor_list[i] for i in range(len(prime_list))]
    answer = reduce(lambda x, y: x * y, l)
    return answer

if __name__=='__main__':
    print(smallest(20))
