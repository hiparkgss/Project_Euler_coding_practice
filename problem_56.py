def digit_sum(n):
    s = str(n)
    return sum(int(char) for char in s)

q = max(digit_sum(a ** b) for a in range(1, 100) for b in range(1, 100))
print(q)