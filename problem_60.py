import functools
import operator
import os
import itertools as it
import time
import networkx as nx

t0 = time.time()
with open('prime_list_comma.csv', 'r') as f:
    a = f.readline().split(',')

prime_list = [int(elem) for elem in a]
prime_set = set(prime_list)


# three_mod_one = [elem for elem in prime_list if elem % 3 == 1]
# three_mod_two = [elem for elem in prime_list if elem % 3 == 2]
# three_mod_one_string = [str(elem) for elem in three_mod_one]
# three_mod_two_string = [str(elem) for elem in three_mod_two]
#
#
# def gen_concat(l):
#     """
#
#     :param l: list of int numbers
#     :return: generate list of concatenated numbers
#     """
#     # first make the list into string for manipulation
#     sl = [str(elem) for elem in l]
#
#     return [int(''.join(t)) for t in it.permutations(sl, 2)]
#
#
# def are_prime(l):
#     """
#
#     :param l: list of int numbers
#     :return: return True if all the numbers are primes
#     """
#     # if max(l) > max(prime_set):
#     #     print('the list contains number beyond the prime set')
#
#     if all(elem in prime_set for elem in l):
#         return True
#     else:
#         return False
#
#
# def is_concat_prime(l, s):
#     """
#     e.g. l = [3, 7]
#     Return True if all of the following conditions are satisfied:
#     '3' + s is prime
#     s + '3' is prime
#     '7' + s is prime
#     s + '7' is prime
#
#     :param list l: list of integers
#     :param str s: integer in string
#     :return bool: boolean.
#
#     Examples:
#         >>> is_concat_prime([3, 7], '109')
#         True
#
#         >>> is_concat_prime([3, 7, 109], '673')
#          True
#
#         >>> is_concat_prime([3, 7], '9')
#         False
#     """
#
#     for elem in l:
#         if int(str(elem) + s) in prime_set:
#             if int(s + str(elem)) in prime_set:
#                 continue
#             else:
#                 return False
#         else:
#             return False
#
#     return True


t2 = time.time()

print('start calculation\n')


############################################################################
# second attempt

def partition_prime_list(arr):
    """
    partition_prime_list function partitions prime numbers and return dict of
    {prime number: [p1, p2]} or empty dict if there is none

    Args:
        arr (:obj:`set of :obj:`int): set of prime numbers to be tested

    Returns:
        dict:
        {prime number: [ {partitioned prime 1, partitioned prime 2},...]} or empty dict

        check that partitioned prime 2 - partitioned prime 1
        (the reverse order) is also prime.

    """

    #########################################
    # beginning of inner function

    def partition_prime(i):
        """
        partitions the input prime.
        this function is useful for the main function.

        Args:
            i: prime integer

        Returns:
            [ (partitioned prime 1, partitioned prime 2),...]
            or [  ] empty list if there is no partitioned prime sets.

        Examples:

            >>> partition_prime(7109)
            [{7, 109}]

            >>> partition_prime(1097)
            [{109, 7}]

            >>> partition_prime(102)
            []

        """
        s = str(i)
        num = len(s)
        result = []

        if num == 1:
            return result

        for i in range(num - 1):
            if s[i + 1] == '0':  # zero digit. need to skip the iteration.
                continue

            p1 = int(s[0:i + 1])
            p2 = int(s[i + 1:])
            reverse_prime = int(s[i + 1:] + s[0:i + 1])

            if reverse_prime in prime_set:
                if p1 in prime_set:
                    if p2 in prime_set:
                        result.append((p1, p2))
                    else:
                        continue
                else:
                    continue
            else:
                continue

        return result

    # end of inner function
    ########################################

    result_set = set()

    for prime_num in arr:
        pp = partition_prime(prime_num)
        if pp:  # partitioned prime pairs exist
            result_set.update(pp)

    # sanity check
    print('the number of partitioned primes:', len(result_set))

    return result_set


# end of function
#######################################

pp_set = partition_prime_list(prime_set)


# making a undirected graph of partitioned primes as nodes and pairs as edges.
G = nx.Graph()
G.add_edges_from(pp_set)

a = nx.find_cliques(G)
a = list(a)
a = [(sum(sublist), sublist) for sublist in a if len(sublist) > 4]
print('ANS. possible set:', a)

# I used mathematica for this question as well.


############################################################################
# failed attempt

"""
# case 1:
# 3, 7, 109, 673 are the initial guess.
# pick 1 more prime number in three_mod_one.
prime_after_concat_set = set()
initial_guess = [3, 7, 109, 673]

# starting after 673, which is three_mod_one_string[57].
for s in three_mod_one_string[58:1000000]:
    if is_concat_prime(initial_guess, s):
        prime_after_concat_set.add(int(s))

if prime_after_concat_set != set():  # not an empty set
    m = min(prime_after_concat_set)
    initial_guess.append(m)
    s = sum(initial_guess)
    print('case 1 \nanswer:', s, '\n\n')
else:  # empty set
    print('case 1 failed', '\n\n')

"""

"""
# case 2:
# 3 is the initial guess.
# pick 4 more prime numbers in three_mod_two
prime_after_concat_set = set()
initial_guess = [3]

# starting from 11, which is three_mod_two_string[2]
for s in three_mod_two_string[2:100]:
    if is_concat_prime(initial_guess, s):
        prime_after_concat_set.add(int(s))

var_num = 5 - len(initial_guess)
for tu in it.combinations(prime_after_concat_set, var_num):
    arg = gen_concat(initial_guess + list(tu))
    if are_prime(arg):
        print("case2\n ans:", sum(arg), '\n')
        print("the prime pair set is:", arg)

print("case 2 failed\n\n")
"""

"""
# case 3:
# initial guess is [7, 109, 673], excluding 3
# pick 2 more prime numbers in three_mod_one
prime_after_concat_set = set()
initial_guess = [7, 109, 673]

# starting after 673, which is three_mod_one_string[57].
for s in three_mod_one_string[58:10000]:
    if is_concat_prime(initial_guess, s):
        prime_after_concat_set.add(int(s))

var_num = 5 - len(initial_guess)
for tu in it.combinations(prime_after_concat_set, var_num):
    arg = gen_concat(initial_guess + list(tu))
    if are_prime(arg):
        print("case3\n ans:", sum(arg), '\n')
        print("the prime pair set is:", arg)

print("case 3 failed \n\n")
"""

"""
# case 4
prime_after_concat_set = three_mod_two[2:100]
initial_guess = []


var_num = 5 - len(initial_guess)
for tu in it.combinations(prime_after_concat_set, var_num):
    arg = gen_concat(list(tu))
    if are_prime(arg):
        print("case4\n ans:", sum(arg), '\n')
        print("the prime pair set is:", arg)

print("case 4 failed \n\n")
"""

"""
# case 5:
prime_after_concat_set = set()
initial_guess = [3, 7]

# starting after 673, which is three_mod_one_string[57].
for s in three_mod_one_string[1:20000]:
    if is_concat_prime(initial_guess, s):
        prime_after_concat_set.add(int(s))

var_num = 5 - len(initial_guess)
for tu in it.combinations(prime_after_concat_set, var_num):
    arg = gen_concat(initial_guess + list(tu))
    if are_prime(arg):
        print("case5\n ans:", sum(arg), '\n')
        print("the prime pair set is:", arg)

print("case 5 failed \n\n")
"""

"""
# case 6:
prime_after_concat_set = set()
initial_guess = [7]

# starting after 673, which is three_mod_one_string[57].
for s in three_mod_one_string[1:500]:
    if is_concat_prime(initial_guess, s):
        prime_after_concat_set.add(int(s))

var_num = 5 - len(initial_guess)
for tu in it.combinations(prime_after_concat_set, var_num):
    arg = gen_concat(initial_guess + list(tu))
    if are_prime(arg):
        print("case6\n ans:", sum(arg), '\n')
        print("the prime pair set is:", arg)

print("case 6 failed \n\n")
# """

t1 = time.time()
print("CPU time spend:", t1 - t0)
print("time for reading file of prime number", t2 - t0)
