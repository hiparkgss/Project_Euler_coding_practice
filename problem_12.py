with open('prime_list_comma.csv', 'r') as f:  # import prime number list
    prime_list_overall = f.readline().split(',')

def triangle_number(n):
    '''

    :param n: int n
    :return: 1+2+...+n

    '''

    return int(n * (n + 1) / 2)

def find_prime(n):
    """

    :param n: integer n
    :return: find prime number below or equal to n
    """
    if n == 1:
        print('input is 1. NO prime under 1')
        raise TypeError

    prime_list = []
    for i in prime_list_overall:
        j = int(i)
        if j <= n:
            prime_list.append(j)  # list of prime under or equal to n

    return prime_list

def factor(n):
    '''

    :param n: integer n
    :return: factor n in dictionary. key is a prime and value is the corresponding exponent.
    '''
    if n == 1:
        return {1: 1}

    prime_list = find_prime(n)

    num_of_prime = len(prime_list)
    factor_dic = {}

    for i in range(num_of_prime):

        counter = 0  # counter for while loop

        while n % prime_list[i] == 0:  # check if n is divisible by i_th prime number
            n = n / prime_list[i]  # update value of n
            counter += 1
            factor_dic[prime_list[i]] = counter

    return factor_dic


from functools import reduce
import operator


def number_of_divisor(n):
    factor_dic = factor(n)
    return reduce(operator.__mul__, [factor_dic[i] + 1 for i in factor_dic])


import time

if __name__ == '__main__':
    t0 = time.time()
    counter = 4
    ans = triangle_number(counter)
    while number_of_divisor(ans) < 500:
        counter += 1
        ans = triangle_number(counter)
    print('The answer is %d, %d th counter' % (ans, counter))

    t1 = time.time()

    print(t1 - t0, 's was spend to run this code')

