from problem_12 import factor
import itertools as it
from functools import reduce
import operator as op

def divisor(n):
    '''

    :param n: integer n
    :return: list of divisor including the number n itself

    '''
    if n == 1:
        return [1]
    factor_dic = factor(n)
    keys_list = list(factor_dic.keys())
    num = len(keys_list)
    if n in keys_list:
        return [1, n]

    exponent_list = [factor_dic[keys_list[i]] + 1 for i in range(num)]
    exponent_range_list = map(range, exponent_list)
    divisor_list = []

    for sublist in it.product(*exponent_range_list):
        divisor_list.append(reduce(op.__mul__, [keys_list[i] ** sublist[i] for i in range(num)]))

    return divisor_list



def d(n):
    '''

    :param n: integer n
    :return: sum of divisor excluding the number n itself
    '''

    divisor_list = divisor(n)
    divisor_list.pop()  # removing the last element

    return sum(divisor_list)


if __name__ == '__main__':
    import time

    t0 = time.time()
    amicable_number_list = [d(i) for i in range(2, 10000 + 1) if d(d(i)) == i and d(i) != i]

    print('The answer is %d' % sum(amicable_number_list))
    print('Amicable numbers are', amicable_number_list)

    t1 = time.time()

    print(t1 - t0, 's was spend to run this code')

