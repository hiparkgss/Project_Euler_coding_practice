import itertools as it

a = list(it.permutations('0123456789', 10))[1000000-1]
b = ''.join(a)
print(b)
