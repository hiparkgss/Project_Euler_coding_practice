import numpy as np
l = np.array(range(1, 101))
sum_of_square = sum(l ** 2)
square_of_sum = sum(l) ** 2
print(square_of_sum - sum_of_square)
