def is_palindrome(n):
    """

    :param n: integer (base 10)
    :return: True or False value of palindrome
    """
    sn = str(n)
    rel = reversed(list(sn))
    return ''.join(rel) == sn

def is_bin_palindrome(n):
    """

    :param n: integer (base 10)
    :return: True or False value of palindrome of number n in base 2
    """
    b = bin(n)[2:]  # string of number in base 2
    rel = reversed(list(b))
    return ''.join(rel) == b

a = sum(n for n in range(1, 10**6 + 1) if is_bin_palindrome(n) and is_palindrome(n))
print(a)