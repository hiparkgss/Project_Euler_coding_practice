n = 1
while 9 ** 5 * n > 10 ** (n-1):
    n += 1

# now n is the smallest integer that satisfies 10^(n-1) > 9^5 n >> giving 7

number = 10  # starting from 2 digit number because it has to be a sum
result = []

while len(str(number)) < n:  # smaller digit than 7.

    digit_sum = sum(int(char) ** 5 for char in str(number))

    if digit_sum == number:
        result.append(number)

    number += 1

print('the answer is ', sum(result))
print('the list of that special number is', result)