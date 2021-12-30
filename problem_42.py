# read the file
with open('p042_words.txt', 'r') as f:
    word_list_overall = f.readline().split(',')

# remove quotation mark
word_list_overall = [elem.strip('"') for elem in word_list_overall]

# alphabet value dictionary
ldic = []
p1 = ord('A') -1
for i in range(1+p1, 26+p1+1):
    ldic.append((chr(i), i-p1))
ad = dict(ldic)

def word_value(s):
    """

    :param s: word in string. only uppercase
    :return: give value using dictionary ad
    """
    v = 0  # starting value is zero. If s is empty, then return zero
    for char in s:
        v += ad[char]

    return v


# estimate the upper bound of the word value given by assuming 'Z' with max length
m = max(len(elem) for elem in word_list_overall) * ad['Z']


def triangle(n):
    return int(n * (n+1)/2)

td = {}  # { triangle(n) : n } upto triangle(n) below max number
n = 1
while triangle(n) < m+1:
    td[triangle(n)] = n
    n += 1


def is_triangle(n):
    return n in td

count = 0
for word in word_list_overall:
    if is_triangle(word_value(word)):
        count +=1

print(count)