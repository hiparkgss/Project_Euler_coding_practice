import math

with open('prime_list_comma.csv', 'r') as f:  # import prime number list
    prime_list_overall = f.readline().split(',')

q = 10000
p = [int(elem) for elem in prime_list_overall if int(elem) < q]  # prime number list
c = [num for num in range(9, q, 2) if num not in p]  # composite number list

def is_square(n):
    return int(math.sqrt(n)) ** 2 == n

for com in c:
    result = False
    for pr in p:
        q1, r = divmod(com - pr, 2)
        if q1 > 0 and r == 0 and is_square(q1):
            result = True
            break

    if not result:
        print(com)
        break