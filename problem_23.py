from problem_21 import d
import time
import itertools as it

t0 = time.time()
abundant_number_list = []

for i in range(1, 28124):
    if d(i) > i:
        abundant_number_list.append(i)

tuple_list = it.product(abundant_number_list, repeat=2)
sum_of_abundant_number_list = list(set(sum(tuple_elem) for tuple_elem in tuple_list))

answer = [i for i in range(1, 28124) if i not in sum_of_abundant_number_list]

print('this is an abundant number list:', abundant_number_list)
print('this is not the sum of abundant number list:', answer)
print('the answer is:', sum(answer))

t1 = time.time()
print(t1 - t0, 's was spend to run this code')