def divide(n, d):
    remainders = []
    count = 0
    while remainders.count(n) < 2 and n != 0:
        n *= 10
        n = n % d
        remainders.append(n)
        count += 1
    return count - remainders.index(n) - 1

maxCycle = 0
maxNum = 0
for denominator in range(1, 1000, 2):
    cycleLength = divide(1, denominator)
    if cycleLength > maxCycle:
        maxCycle = cycleLength
        maxNum = denominator
print(maxNum)