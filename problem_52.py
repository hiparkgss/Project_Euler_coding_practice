n = 100

def is_multiple_permutation(n):
    ln = len(str(n))
    a = [set(str(i * n)) for i in range(2, 7)]
    b = [len(elem) == ln for elem in a]
    c = [a[0]==elem for elem in a]
    return all(b) and all(c)

while True:
    if is_multiple_permutation(n):
        print(n)
        break
    n += 1