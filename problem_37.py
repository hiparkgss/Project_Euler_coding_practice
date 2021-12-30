import itertools as it
import math as m

with open('prime_list_comma.csv', 'r') as f:  # import prime number list
    prime_list_overall = f.readline().split(',')

def twodigit():
    """

    :return: return numbers with 3, 7 only
    """
    return [10 * i + j for i in [2, 3, 5, 7] for j in range(3, 8, 2)]

def ndigit(n):
    """

    :param n: integer bigger than 2: 3, 4, 5, ...
    :return: give n digit number using 3, 5, 7 at the ends and 1, 3, 5, 7, 9 for the rest of the digit
    """

    str_twodigit = [str(elem) for elem in twodigit()]
    l = [''.join(elem) for elem in it.product(['1', '3', '7', '9'], repeat=n-2)]

    return [int(elem[0] + subl + elem[1]) for elem in str_twodigit for subl in l]

def truncate(n1):
    """

    :param n1: integer
    :return: truncate n and output lists
    """
    s = str(n1)
    l = len(s)
    return [s[i:] for i in range(l)] + [s[0:i] for i in range(1, l)]

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


result = []
for n in range(2, 7):
    for i in ndigit(n):
        if all(is_prime(int(j)) for j in truncate(i)):
            result.append(i)

print('the list of truncatable primes is', result)
print('the answer is ', sum(result))


