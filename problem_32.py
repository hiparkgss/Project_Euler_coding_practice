import itertools as it

result = []

def list_to_number(l):
    """

    :param l: list. e.g. [1,2,3,4]
    :return: integer 1234
    """
    if type(l) == int:
        return l

    l.reverse()
    return sum(10 ** i * v for i, v in enumerate(l))


p = it.permutations(range(1, 10))

if __name__ == '__main__':
    for subtuple in p:
        sublist = list(subtuple)
        # one digit * four digit = four digit
        if list_to_number(sublist[0]) * list_to_number(sublist[1:5]) - list_to_number(sublist[5:9]) == 0:
            result.append(list_to_number(sublist[5:9]))

        # 2 digit * 3 digit = four digit
        elif list_to_number(sublist[0:2]) * list_to_number(sublist[2:5]) - list_to_number(sublist[5:9]) == 0:
            result.append(list_to_number(sublist[5:9]))

    print(sum(set(result)))