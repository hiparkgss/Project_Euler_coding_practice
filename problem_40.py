from functools import reduce
from operator import __mul__

s = '0'
for i in range(1, 300000):
    s += str(i)

print(reduce(__mul__, map(int, [s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]])))
