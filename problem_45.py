import sys

def h(n):
    return 2*n*(2*n-1)

def p(n):
    return n*(3*n-1)

n = 144
m = 166
while True:
    while p(m) < h(n):
        m += 1
        if p(m) == h(n):
            print(h(n)/2)
            sys.exit()
    n += 1

