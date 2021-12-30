import itertools

with open('p059_cipher.txt', 'r') as f:  # the file is a single line txt file.
    file = f.readline().rstrip().split(',')  # list of str

l = [int(i) for i in file]  # list of int numbers of encrypted message


def key_xor_single_char(num, char):
    """

    :param num: int number
    :param char: single character in str
    :return: return xor value
    """
    return chr(num ^ ord(char))


def key_open(li, letter):
    """

    :param li: list of int number
    :param letter: three letter consisting of characters
    :return: cyclic key_xor value
    """
    return ''.join([key_xor_single_char(elem, letter[i % 3]) for i, elem in enumerate(li)])


stan = ord('a')
lin = itertools.product([chr(elem) for elem in range(stan, stan+26)], repeat=3)
a = [''.join(elem) for elem in lin]

count = 0
for elem in a:
    c = key_open(l, elem).count('the')
    if c > count:
        count = c
        k = elem

m = key_open(l, 'god')
# print('k', k, '\ncount', count)
# print('ans', key_open(l, 'god'))
print(sum(ord(char) for char in m))
