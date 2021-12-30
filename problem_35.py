from problem_12 import find_prime

p_list = find_prime(10 ** 6)
print('prime list is ', p_list)


def circulate(p):
    """

    :param p: integer
    :return: yield possible circulates. generator object
    """
    cir = []
    sp = str(p)
    digit_num = len(sp)
    for i in range(digit_num):
        cirps = sp[i:digit_num] + sp[0:i]
        cir.append(int(cirps))
    return list(set(cir))

result = []
while p_list:
    p1 = p_list[-1]
    # print('p1 is', p1)
    sp1 = str(p1)

    if any(d in sp1 for d in '024685'):
        p_list.pop()
        continue

    if p1 in result:
        p_list.pop()
        continue

    lp = circulate(p1)
    # print('lp is ', lp)
    if all(elem in p_list for elem in lp):
        # print('if part activated')
        for elem in lp:
            result.append(elem)
        p_list = [primes for primes in p_list if primes not in lp]
        # print('result at this point is', result)

    else:
        p_list.pop()

    # print('p_list at this point is', p_list)



flatten = result + [2, 5]
print(len(flatten))
# print('this is flatten', flatten)