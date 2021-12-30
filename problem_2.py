def fibonacci(n):
    """
    (int) -> int

    >>> fibonacci(10)
    89
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 1
result = 0
while fibonacci(n) <= 4000000:
    if fibonacci(n) % 2 == 0:
        result += fibonacci(n)
    n += 1

print(result)
