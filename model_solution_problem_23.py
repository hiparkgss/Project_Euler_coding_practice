def sumdivs(n):
    return 1 + sum([i, i+n//i][i!=n//i] for i in range(2, int(n**.5)+1) if n % i == 0)

a=[0]*2+[sumdivs(i)>i for i in range(2,28123)]

def cannot(n):
    return not any(a[i] and a[n-i] for i in range(n//2+1))
print(sum(i for i in range(28123) if cannot(i)))