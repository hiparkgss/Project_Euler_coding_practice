import time


t0 = time.time()

fibonacci_list = [0, 1]

def fibonacci(n):
    """

    :param n: integer n
    :return: n_th fibonacci number
    """

    while n + 1 > len(fibonacci_list):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list[n]

print('test for 5th finobacci number', fibonacci(5))

n=1

while len(str(fibonacci(n))) < 1000:
    n += 1

print('the answer is', n)

t1 = time.time()
print(t1 - t0, 's was spend to run this code')