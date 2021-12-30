from itertools import permutations

def tu_to_s(tu):
    """

    :param tu: tuple of integers
    :return: make them in a string
    """
    s = ''
    for element in tu:
        s += str(element)
    return s

l = []
for tunum in permutations(range(10)):
    s = tu_to_s(tunum)
    if int(s[3]) % 2 == 0 and int(s[5]) % 5 == 0:
        if all([int(s[2:5]) % 3 == 0, int(s[4:7]) % 7 == 0, int(s[5:8]) % 11 == 0,
               int(s[6:9]) % 13 == 0, int(s[7:]) % 17 == 0]):
            l.append(int(s))

print(l)
print(sum(l))


