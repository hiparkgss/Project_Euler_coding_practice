import numpy as np
import time

t0 = time.time()

"""
Mathematical analysis.

xk/(sqrt n - yk) is the basic form. 

From simple symbolic algebra, the followings are found:
x_(k+1) = (n - yk^2) / xk
y_(k+1) = a_(k+1) * x_(k+1) - yk
a_(k+1) = floor(xk / (sqrt n - yk))

x0 = 1
y0 = a0 = floor(sqrt n)


"""

def biggest_square_below(arr):
    """

    Args:
        arr: numpy array of int

    Returns:
        np.array
        array[0] = the biggest integer equal or less than the sqrt of each element.
        array[1] = input arr without square number.
        array[2] = float: sqrt of arr

    """

    sqrt_arr = np.sqrt(arr)
    floor_arr = np.floor(sqrt_arr)
    no_sq_arr = arr[floor_arr != sqrt_arr]
    sqrt_arr = np.sqrt(no_sq_arr)
    sqrt_int_arr = sqrt_arr.astype(np.int)

    return np.array([sqrt_int_arr, no_sq_arr, sqrt_arr])


def continued_fraction(arr):
    """

    Args:
        arr: numpy array biggest_square_below result

    Returns:
        np.array of the following:

                a0   a1    a2    ....  a_1000
              ____________________________
        arr[0]|
        arr[1]|
        arr[2]|
            . |
            . |
            . |

    """

    y = arr[0, :]
    a = y[:]
    n = arr[1, :]
    sqrt_n = arr[2, :]
    row_n = len(a)
    col_n = 1001
    x = np.ones(row_n)
    result = np.zeros([row_n, col_n])

    for i in range(col_n):
        result[:, i] = a

        a = np.floor(x / (sqrt_n - y))  # a_k+1 update
        x = (n - y ** 2)/x  # x_k+1 update
        y = a * x - y  # y update

    return result

def period_of_cycle(arr):
    """

    Args:
        arr: np.array
        the result of continued_fraction function

    Returns:
        np.array
        period in int
        [period of arr[0], period of arr[1], ...]

    """
    row_num, col_num = arr.shape
    period = []

    def get_period(arr):
        """

        Args:
            arr: 1 - D np.array

        Returns:
            int
            period of the array

        """
        period_len = len(arr) - 1
        l = 1  # maximum detectable period length
        while True:
            r_n = period_len // l
            arr_reshape = np.reshape(arr[1: r_n * l + 1], (r_n, l))
            if np.all(arr_reshape == arr_reshape[0, :]):
                return l
            else:
                l += 1

    for row in range(row_num):
        period.append(get_period(arr[row, :]))

    return np.array(period)

################################################
# main function

nlim = 10 ** 4

arr_input = np.arange(2, nlim + 1)
bsb_arr = biggest_square_below(arr_input)
cf_arr = continued_fraction(bsb_arr)
poc_arr = period_of_cycle(cf_arr)

odd_period_arr = poc_arr[poc_arr % 2 == 1]
ans = len(odd_period_arr)
print('ans', ans)

t1 = time.time()
print('computational time', t1 - t0)




