import math

def is_prime(n):
    """

    :param n: integer n
    :return: True or False

    >>> is_prime(39)
    False

    >>> is_prime(1097)
    True

    """
    if n != int(n):  # integer input only
        raise ValueError('input is not an integer')

    else:
        if n % 6 in {1, 5}:  # remainder should be either 1 or 5 to be a prime
            for i in range(5, int(math.sqrt(n))+ 1):  # upto sqrt(n)
                if n % i == 0:
                    return False

            return True

        else:
            return False

