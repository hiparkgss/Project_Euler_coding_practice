import numpy as np
from functools import reduce
import operator as op
file = "problem_11_grid.txt"

with open(file) as f:
    l = np.array([np.fromstring(line, sep=' ', dtype=int) for line in f.readlines()])


def pi(ar):
    '''

    :param ar: input np array of size 4
    :return: product of them

    '''

    return reduce(op.__mul__, ar)

def side_product(ar):

    '''

    :param ar: input np array
    :return: output maximum of the product

    '''

    col_length = ar.shape[1]
    row_length = ar.shape[0]
    pd = []
    for j in range(row_length):
        for i in range(col_length-4):
            pd.append(pi(ar[j, i:i+4]))

    return max(pd)

def vertical_product(ar):

    col_length = ar.shape[1]
    row_length = ar.shape[0]
    pd = []
    for j in range(col_length):
        for i in range(row_length - 4):
            pd.append(pi(ar[j, i:i + 4]))

    return max(pd)

def diagonal_right(ar):

    col_length = ar.shape[1]
    row_length = ar.shape[0]
    pd = []
    for j in range(col_length-4):
        for i in range(row_length - 4):
            pd.append(ar[i, j] * ar[i+1, j+1] * ar[i+2, j+2] * ar[i+3, j+3])

    return max(pd)


def diagonal_left(ar):
    col_length = ar.shape[1]
    row_length = ar.shape[0]
    pd = []
    for j in range(4, col_length):
        for i in range(0, row_length-4):
            pd.append(ar[i, j] * ar[i + 1, j - 1] * ar[i + 2, j - 2] * ar[i + 3, j - 3])

    return max(pd)

print(max([side_product(l), vertical_product(l), diagonal_left(l), diagonal_right(l)]))

