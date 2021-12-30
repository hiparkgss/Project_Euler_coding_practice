import decimal as dec

# setting 100 significant figures below decimal point
precision = 2000
dec.getcontext().prec = precision


def first_cycle(l):
    """
    check if there is a cycle from the beginning and return the cycle.
    cycle exist if it is repeated more than once.
    exception may be raised for the last few elements
    If there is no cycle, return False.

    :param l: input list.
    :return: cyclic part of the list

    >>> first_cycle(['6','6','6','6','6','6','6','6'])
    (True, ['6'])

    >>> first_cycle([1, 2, 3, 1, 2, 3, 1, 2])
    (True, [1, 2, 3])

    >>> first_cycle(['1', '2', '3', '1', '2', '3', '1', '2'])
    (True, ['1', '2', '3'])

    >>> first_cycle([1, 1, 1, 1])
    (True, [1])

    >>> first_cycle([1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1])
    (True, [1, 1, 2])

    >>> first_cycle([1, 2, 2, 3, 4])
    (False, None)

    >>> first_cycle([2, 2, 7, 2, 7, 2])
    (False, None)
    """
    # initialisation of index for the following while loop
    finding_cycle = 1
    n_list = len(l)
    try:
        while True:
            # find the index of the possible next cycle
            cycle_num = l.index(l[0], finding_cycle)  # the same value as the length of the cycle

            # create a boolean list that compare each digit of the first cycle and the next one
            if cycle_num * 2 < n_list - 1:  # for the case of [2,2,7,2]... this prevents IndexError
                bool_list = [l[k] == l[k + cycle_num] for k in range(cycle_num)]
            else:
                return False, None

            # need to avoid the case of '1113 1113 1113 ....'
            # so check if the cycle found is correct for the rest of the 100 digits.
            if all(bool_list):
                cycle_rep = n_list // cycle_num  # number of repeated cycle
                check_bool_list = [l[j + cycle_num * i] == l[j + cycle_num * (i + 1)]
                                   for i in range(cycle_rep - 1)  # between cycle i and i+1
                                   for j in range(cycle_num)]  # sweeping the cycle

                if all(check_bool_list):  # the answer. return this answer in str format
                    return True, l[0:cycle_num]
                else:
                    finding_cycle += 1

            else:
                finding_cycle += 1

    # except command is to catch the number that does not have recurring cycle.
    except ValueError:
        return False, None


def check_cycle(n):
    """
    :param n: input decimal.Decimal n
    :return: output the cyclic part as a string
    """
    #  process number into list, while deleting 0 and decimal point.
    #  remove zeros that come right after decimal point with while loop.
    num_list = list(str(n)[2:])
    while num_list[0] == '0':
        num_list.remove('0')

    n_list = len(num_list)

    # assuming that the recurring cycle starts from the beginning of nonzero element
    counter = 0  # initialise of counter
    while counter < n_list-1:  # ignoring the last element that is rounded. 1/6 = 0.1666667
        a = first_cycle(num_list[counter:n_list - 1])
        if a[0]:
            return ''.join(a[1])  # return the recurring cycle in string. e.g. '1234'
        else:
            counter += 1

    # for the case of not finding recurring cycle:
    print('%s may exceed %d recurring cycle' % (n, precision))


if __name__ == '__main__':
    ans_list = []
    for i in range(3, 1001):
        division = dec.Decimal(1) / dec.Decimal(i)  # number in exact.
        if len(str(division)) > precision:
            a = check_cycle(division)
            ans_list.append((i, a, len(a)))  # removing 2 and 5 multiples... like 10, 25...
            # (i for 1/i, a for recurring cycle, length of cycle)
    final = sorted(ans_list, key=lambda elem: elem[2], reverse=True)
    print('These are the length of recurring cycle: ', [elem[2] for elem in final[0:4]])
    print('the answer is %s with the length %d' % (final[0][0], final[0][2]))
