import csv

def find_prime(n):
    '''

    :param n: int n
    :return: list of a prime number under integer n
    '''

    bool_list = [True] * (n+1)  # create a list of boolean to check prime number
    bool_list[0:2] = [False, False]  # index matches the number. 0 and 1 is not prime so false
    for i in range(n+1):
        if bool_list[i]:  # if it is a prime number, it gives True
            for j in range(2*i, n+1, i):  #  for the multiples of the prime number are assigned the value False
                bool_list[j] = False

        else:
            continue

    return [i for i in range(n+1) if bool_list[i]]

if __name__ == '__main__':
    prime_list = find_prime(10 ** 8)

    with open('prime_list_comma.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(prime_list)