with open('prime_list_comma.csv', 'r') as f:
    prime_overall_list = f.readline().split(',')

m = 1000000
p = [int(elem) for elem in prime_overall_list if int(elem) < m]

def prime_factor(n):
    a = set()
    q = n
    for prime in p:

        if prime > q:
            return a

        r = q % prime

        if r == 0:
            a.add(prime)
            q = q//prime


n = 647
while True:
    l = (n, n+1, n+2, n+3)
    if all(len(prime_factor(num)) == 4 for num in l):
        print(n)
        break
    n += 1


