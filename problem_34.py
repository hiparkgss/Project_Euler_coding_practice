import itertools as it
from problem_32 import list_to_number

factorial = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

result = []


two_digit = it.product(range(5), repeat=2)
three_digit = it.product(range(7), repeat=3)
four_digit = it.product(range(8), repeat=4)
five_digit = it.product(range(9), repeat=5)
six_digit = it.product(range(10), repeat=6)
seven_digit = it.product(range(10), repeat=7)


def result_append(digit_num):
    for num_tuple in digit_num:
        numdigit = list_to_number(list(num_tuple))
        facnum = sum(factorial[d] for d in num_tuple)
        if numdigit == facnum and num_tuple[0] > 0:
            result.append(numdigit)

    return None


[result_append(arg1) for arg1 in [two_digit, three_digit, four_digit, five_digit, six_digit, seven_digit]]



print('this is the result', result)
