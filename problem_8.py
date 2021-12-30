import numpy as np
from functools import reduce
import operator

num = np.loadtxt('number from web.txt', delimiter='\n', dtype=str)
number_str = reduce(lambda x, y: x + y, num)
result = 0
for i in range(1000-12+1):
    number_list = np.array(list(number_str[i:i + 13]), dtype=int)
    mul = reduce(operator.mul, number_list)
    if result <= mul:
        result = mul
print(result)
