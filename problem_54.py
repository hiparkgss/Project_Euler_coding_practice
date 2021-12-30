import requests

r = requests.get("https://projecteuler.net/project/resources/p054_poker.txt")
data = r.content  # Content of response
data_s = str(data).strip("' b")  # remove ' and b sign at the both ends
d = data_s.split('\\n')  # splitting with \n sign
d = d[:-1]  #  removing the empty string at the last
ll = [elem.split() for elem in d]
sl = [(sublist[0:5], sublist[5:]) for sublist in ll]
print(sl)

def analyse_card(l):
    """

    :param l: list of card in string
    :return: ranking of card
    """
    suit = {}
    number = {}
    for elem in l:
        if elem[0] in number:
            number[elem[0]] += 1
        else:
            number[elem[0]] = 1

        if elem[1] in suit:
            suit[elem[1]] += 1
        else:
            suit[elem[1]] = 1

    return suit, number

def analyse_card_to_numbers(t):
    d1 = t[1]
    ed = {}
    for k in d1:
        if k == 'T':
            ed[10] = d1[k]
        elif k == 'J':
            ed[11] = d1[k]
        elif k == 'Q':
            ed[12] = d1[k]
        elif k == 'K':
            ed[13] = d1[k]
        elif k == 'A':
            ed[14] = d1[k]
        else:
            ed[int(k)] = d1[k]

    return t[0], ed


def is_flush(t):
    return 5 in t[0].values()

def is_four_kind(t):
    return 4 in t[1].values()

def is_three_kind(t):
    return 3 in t[1].values()

def is_pair(t):
    return 2 in t[1].values(), [i for i in t[1] if t[1][i] == 2]

def is_double_pair(t):
    return is_pair(t)[0] and len(t[1])==3

def is_high_card(t):
    return (not is_flush(t)) and len(t[1].values()) == 5, max(t[1].keys())

def is_straight(t):

    if len(t[1].keys()) == 5:
        temp_l = list(t[1].keys())
        temp_l.sort()
        return all([elem - i == temp_l[0] for i, elem in enumerate(temp_l)])

    return False

def is_straight_flush(t):
    return is_flush(t) and is_straight(t)

def is_royal_flush(t):
    a = []
    for i in range(10, 15):
        a.append(i in t[1].keys())
    return all(a) and is_straight_flush(t)

def is_full_house(t):
    return is_pair(t)[0] and is_three_kind(t)

def card_score(l):
    """

    :param l: list
    :return: score
    """
    t = analyse_card_to_numbers(analyse_card(l))

    if is_royal_flush(t):
        return 'royal flush',
    elif is_straight_flush(t):
        return 'straight flush',
    elif is_four_kind(t):
        return 'four of a kind',
    elif is_full_house(t):
        return 'full house',
    elif is_flush(t):
        return 'flush',
    elif is_straight(t):
        return 'straight',
    elif is_three_kind(t):
        return 'three of a kind',
    elif is_double_pair(t):
        return 'two pairs',
    elif is_pair(t)[0]:
        return 'one pair', is_pair(t)[1][0]
    elif is_high_card(t)[0]:
        return 'high card', is_high_card(t)[1]
    else:
        raise ValueError('bug fix')

def score_func(s):
    d = {'royal flush': 10, 'straight flush': 9, 'four of a kind': 8, 'full house': 7, 'flush': 6,
         'straight': 5, 'three of a kind': 4, 'two pairs': 3, 'one pair': 2, 'high card': 1}
    return d[s[0]]


count = 0
draw = []
c = 0
weird = []
lose = []
for tu in sl:
    if score_func(card_score(tu[0])) > score_func(card_score(tu[1])):
        count += 1
    elif score_func(card_score(tu[0])) == score_func(card_score(tu[1])):
        if card_score(tu[0])[1] > card_score(tu[1])[1]:
            count += 1
        elif card_score(tu[0])[1] == card_score(tu[1])[1]:
            draw.append(tu)
        elif card_score(tu[0])[1] < card_score(tu[1])[1]:
            c += 1
            lose.append(tu)
        else:
            weird.append(tu)
    else:
        c += 1
        lose.append(tu)

print(count)

