import numpy as np
import itertools as it


# function for generating triangular number and so on
def get_three(n):
    return int(n * (n + 1) / 2)


def get_four(n):
    return n * n


def get_five(n):
    return int(n * (3 * n - 1) / 2)


def get_six(n):
    return n * (2 * n - 1)


def get_seven(n):
    return int(n * (5 * n - 3) / 2)


def get_eight(n):
    return n * (3 * n - 2)


def get_num(inte, n):
    if inte == 3:
        return get_three(n)
    elif inte == 4:
        return get_four(n)
    elif inte == 5:
        return get_five(n)
    elif inte == 6:
        return get_six(n)
    elif inte == 7:
        return get_seven(n)
    elif inte == 8:
        return get_eight(n)
    else:
        raise TypeError('the first input of get_num should be between 3 and 8')


# find four-digit triangular numbers and so on
i = 10 ** 4
three_with_four_digit = [get_three(j) for j in range(i) if 10 ** 3 < get_three(j) < 10 ** 4]
four_with_four_digit = [get_four(j) for j in range(i) if 10 ** 3 < get_four(j) < 10 ** 4]
five_with_four_digit = [get_five(j) for j in range(i) if 10 ** 3 < get_five(j) < 10 ** 4]
six_with_four_digit = [get_six(j) for j in range(i) if 10 ** 3 < get_six(j) < 10 ** 4]
seven_with_four_digit = [get_seven(j) for j in range(i) if 10 ** 3 < get_seven(j) < 10 ** 4]
eight_with_four_digit = [get_eight(j) for j in range(i) if 10 ** 3 < get_eight(j) < 10 ** 4]

# making a tuple of partitioned 2 digit numbers.
three_ab = [(int(str(i)[:2]), int(str(i)[2:])) for i in three_with_four_digit]
four_ab = [(int(str(i)[:2]), int(str(i)[2:])) for i in four_with_four_digit]
five_ab = [(int(str(i)[:2]), int(str(i)[2:])) for i in five_with_four_digit]
six_ab = [(int(str(i)[:2]), int(str(i)[2:])) for i in six_with_four_digit]
seven_ab = [(int(str(i)[:2]), int(str(i)[2:])) for i in seven_with_four_digit]
eight_ab = [(int(str(i)[:2]), int(str(i)[2:])) for i in eight_with_four_digit]

# among eight_ab, some eight_b are in three_a
three_a = {tu[0] for tu in three_ab}
eight_ab_filter_three = {tu for tu in eight_ab if tu[1] in three_a}


###################################################
def filter_cyclic(l1, l2):
    """
    filters the integers in l1 such that the last 2 digit of l1 is in the set of first 2 digit of l2.

    Args:
        l1: list of int
        l2: list of int

    Returns:
        list
        filtered l1 and relevant l2 are returned.

    """

    l2_a_set = {int(str(j)[:2]) for j in l2}
    l1_filtered = [elem for elem in l1 if int(str(elem)[2:]) in l2_a_set]
    l1_b_set = {int(str(j)[2:]) for j in l1_filtered}
    l2_filtered = [elem for elem in l2 if int(str(elem)[:2]) in l1_b_set]
    return l1_filtered, l2_filtered


###################################################

# filtering
eight_filtered, three_filtered = filter_cyclic(eight_with_four_digit, three_with_four_digit)
three_filtered, four_filtered = filter_cyclic(three_filtered, four_with_four_digit)
four_filtered, five_filtered = filter_cyclic(four_filtered, five_with_four_digit)
five_filtered, six_filtered = filter_cyclic(five_filtered, six_with_four_digit)
six_filtered, seven_filtered = filter_cyclic(six_filtered, seven_with_four_digit)
seven_filtered, eight_filtered = filter_cyclic(seven_filtered, eight_filtered)

# ordering
p = np.array(range(6))
ordering = list(it.permutations(p))


###################################################
def filter(l, *four_digits):
    """

    Args:
        l: list of ordering
        *four_digits: actual four-digit numbers

    Returns:
        a list of cyclic numbers
        empty list if they do not exist.

    """
    # sanity check
    number_of_args = len(four_digits)
    number_of_ordering = len(l)
    if number_of_ordering != number_of_args:
        raise TypeError('number of arguments is wrong in filter function')

    # artificially insert the first element to the last of the list
    l = list(l) + [l[0]]

    # four_digits_filtered is a nested lists of the filtered object
    four_digits_filtered = [[]] * number_of_args

    four_digits_filtered[l[0]] = four_digits[l[0]][:]

    for k in range(number_of_args):
        four_digits_filtered[l[k]], four_digits_filtered[l[k + 1]] = filter_cyclic(four_digits_filtered[l[k]], four_digits[l[k + 1]])

    return four_digits_filtered


###################################################


for elem in ordering:

    a = filter(elem, three_with_four_digit, four_with_four_digit, five_with_four_digit, six_with_four_digit,
               seven_with_four_digit, eight_with_four_digit)

    # check if all the filtered lists are non empty
    if all(ele for ele in a):
        # print('a', a)
        b = filter(elem, *a)
        if all(ele for ele in b):
            # print('b', b)
            c = filter(elem, *b)
            if all(ele for ele in c):
                print('c', c)

print('ans', sum(e for sublist in c for e in sublist))