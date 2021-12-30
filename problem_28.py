"""
The diagonal numbers have rules:

1
3^2, 7, 5, 3   difference is 2
5^2, 21, 17, 13    difference is 4

for 1001 by 1001 matrix, the numbers proceed to 1001^2.
"""

odd_list = range(3, 1002, 2)

print(sum(4 * square ** 2 - 6 * (square - 1) for square in odd_list) + 1)