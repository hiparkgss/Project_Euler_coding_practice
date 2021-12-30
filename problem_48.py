def d(n):
    return n ** n % 10 ** 10

print(sum(d(n) for n in range(1, 1001)))