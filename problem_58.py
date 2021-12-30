from os import abort
import math as m

with open('prime_list_comma.csv', 'r') as f:
    prime_overall_list = f.readline().split(',')

prime_list_overall = [int(i) for i in prime_overall_list]

def is_prime(n):
    """
    checking if n is prime

    :param n: integer n
    :return: True or False
    """
    if n == 2:
        return True
    elif n == 1:
        return False
    number_max = int(m.sqrt(n))+1
    if int(prime_list_overall[-1]) < number_max:
        print("input integer n is beyond the range")
        raise ValueError
    ind = 0
    prime_list = []

    # find the index of a prime list that the max prime in the list is just over the number_max
    # given number_max=7, ind = 4 for list [2, 3, 5, 7,  11, ...]
    while True:
        prime = int(prime_list_overall[ind])
        if prime <= number_max:
            ind += 1
            prime_list.append(prime)
        else:
            break

    if any(n % i == 0 for i in prime_list):
        return False
    else:
        return True

counter = 3
i = 3
while 10 * counter > 2 * i - 1:
    i += 2
    s = {i ** 2 - (i - 1), i ** 2 - 2 * (i - 1), i ** 2 - 3 * (i - 1)}
    for elem in s:
        if is_prime(elem):
            counter += 1

print(i)