with open('prime_list_comma.csv', 'r') as f:
    prime_overall_list = f.readline().split(',')

prime = [int(elem) for elem in prime_overall_list if int(elem) < 10 ** 6]
pset = set(prime)
m = len(prime)
n = 22
a = 1
for n in range(400, 1000):
    for i in range(500):
        if sum(prime[i:i + n]) in pset:
            a = (sum(prime[i:i + n]), i, i+n), n
print(a)

