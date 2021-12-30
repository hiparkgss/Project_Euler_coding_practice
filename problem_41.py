import math as m
import itertools as it

with open('prime_list_comma.csv', 'r') as f:  # import prime number list
    prime_list_overall = f.readline().split(',')

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
for i in range(3, 10):
    for t in it.permutations(range(1, i+1)):  # using numbers only upto i
        pandigit = int(''.join(str(char) for char in t))
        if pandigit % 6 == 1 or pandigit % 6 == 1:
            if is_prime(pandigit):
                result.append(pandigit)

# print('all pandigit prime numbers are ', result)
print('the answer is ', max(result))