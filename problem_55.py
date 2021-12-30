def iteration(n):
    s = str(n)
    sr = s[::-1]
    return int(s) + int(sr)

def is_palindrome(n):
    s = str(n)
    sr = s[::-1]
    return s == sr


def is_lychrel(i):
    n = 0
    while n < 50:
        i = iteration(i)
        if is_palindrome(i):
            return False
        n += 1

    return True


count = 0
for i in range(1, 10001):
    if is_lychrel(i):
        count += 1

print(count)