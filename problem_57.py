import fractions as fr
import sys

x = 1 + fr.Fraction(1/2)
def f(n):
    """

    :param n: fractions.Fraction
    :return: recursion
    """

    return 1 + 1/(1 + n)

counter = 0
for i in range(1000):
    x = f(x)
    n = len(str(x.numerator))
    d = len(str(x.denominator))
    if n > d:
        counter += 1

print("counter:", counter)
