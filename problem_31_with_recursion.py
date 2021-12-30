arg2 = [1, 2, 5, 10, 20, 50, 100, 200]
ncoin = len(arg2)
arg3 = [0] * ncoin  # initial start of 0 money
arg1 = 200  # 200 p as in the problem

result_list = []

def ways(amount, value, coin):
    """
    number of ways that amount is divided with value

    :param coin: current coin in the pocket
    :param amount: total amount of money to divide. int type
    :param value: list of available coins
    :return: coin
    """

    if not value:
        return 0

    if amount == 0:
        result_list.append(coin)
        return 0


    while amount < value[-1]:  # selecting the most expensive coin
        # print('the amount is ', amount)
        a = value.pop()
        # print('this is a', a)

    if amount > 0:
        value1 = value[:]
        coin1 = coin[:]
        ind = len(value1) - 1
        coin1[ind] += 1  # adding one to the coding list
        big = value.pop()
        # print('this is big', big)
        return ways(amount, value, coin) + ways(amount - big, value1, coin1)

    else:
        print('else activated')
        return 0

ways(arg1, arg2, arg3)
print(len(result_list))



