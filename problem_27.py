from problem_12 import find_prime
import time

t0 = time.time()
b_list = find_prime(1000)  # list of prime number under 1000

a_list = range(-1001, 1001)
p_list = find_prime(2001000)
# maximum number p_gen can get is n=a=b=1000
#  because whatever n is, n=1000 is not prime

def p_gen(n, a, b):
    """

    :param n: integer n starting from 0
    :return: n^2+an+b form
    """
    return n ** 2 + a * n + b

mx = 0
for b in b_list:
    for a in a_list:
        n = 0
        while p_gen(n, a, b) in p_list:
            n += 1
        if n > mx:
            mx = n
            mxa = a
            mxb = b

print('The answer: (max a, max b, product)', (mxa, mxb, mxa * mxb))
t1 = time.time()

print('The execution time in second is: ', t1-t0)