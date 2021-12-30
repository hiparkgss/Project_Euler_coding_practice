import numpy as np
import time

t0 = time.time()

file = 'p102_triangles.txt'

with open(file) as f:
    triangle_list = f.read().split()

triangle_arr = np.array([int(i) for elem in triangle_list for i in elem.split(',')])
triangle_arr = triangle_arr.reshape(1000, 6)


def solve(m):
    """
    사선식 풀이
    Args:
        m (np.ndarray): each row represent x1, y1, x2, y2, x3, y3

    Returns:
        True if the triangle formed by the row contains the origin
    """
    x1 = m[:, 0]
    y1 = m[:, 1]
    x2 = m[:, 2]
    y2 = m[:, 3]
    x3 = m[:, 4]
    y3 = m[:, 5]

    # area of 012
    area1 = 0.5 * np.abs(x1 * y2 - x2 * y1)

    # area of 023
    area2 = 0.5 * np.abs(x2 * y3 - x3 * y2)

    # area of 031
    area3 = 0.5 * np.abs(x3 * y1 - x1 * y3)

    # area of 123
    area4 = 0.5 * np.abs(x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3)

    # check if the sum of area 123 is equal to area4
    return area1 + area2 + area3 == area4

b = solve(triangle_arr)
ans = np.sum(b)
print(ans)
############################################################################

t1 = time.time()
print('computational time:', (t1-t0) * 1000, 'ms')