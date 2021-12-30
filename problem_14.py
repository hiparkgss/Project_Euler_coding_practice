def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
            sequence.append(n)
        elif n % 2 == 1:
            n = 3 * n +1
            sequence.append(n)
        else:
            print('Bugs!')

    return sequence

import time

t0 = time.time()
data = [len(collatz_sequence(i)) for i in range(1, 1000001)]
print(data.index(max(data)))
t1 = time.time()
print(t1-t0, 'seconds were spent on running this code')