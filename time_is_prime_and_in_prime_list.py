"""
Conslusion:
in prime_set is the fastest way to test a prime number
100 times slower is is_prime
10,000 times slower is in prime_list
"""


import time
from is_prime import is_prime

t0 = time.time()
with open("prime_list_comma.csv") as f:
    a = f.readline().split(',')
    prime_list = [int(prime) for prime in a]
    prime_set = set(prime_list)
    number_of_prime = len(prime_set)

t0 = time.time() - t0  # end of measuring time spent for reading files
print("CPU time for reading files: t0 =", t0)
print("number_of_prime = ", number_of_prime)

# make test list
small_numbers = list(range(100))
large_numbers = prime_list[number_of_prime-100: number_of_prime]

def main_func(test_list):
    """

    :param test_list: list of integers
    :return: time spend
    """

    # start of is_prime()
    t1 = time.time()
    for i in test_list:
        result = is_prime(i)

    t1 = time.time() - t1


    # start of in prime set
    t2 = time.time()
    for i in test_list:
        result = i in prime_set

    t2 = time.time() - t2


    # start of in prime list
    t3 = time.time()
    for i in test_list:
        result = i in prime_list

    t3 = time.time() - t3

    print("\nis_prime: t1 =", t1)
    print("in prime_set: t2 =", t2)
    print("in prime_list: t3 =", t3)
    return None

if __name__ == '__main__':
    main_func(small_numbers)
    main_func(large_numbers)
