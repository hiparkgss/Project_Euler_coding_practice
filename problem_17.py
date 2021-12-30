import csv

with open('problem_17_table.csv', encoding='utf-8', newline='') as file:
    read = csv.reader(file)
    data = []
    for row in read:
        data.append(row)

data[0][0] = '1'

num_row = len(data)

data_dic = {data[i][0]: data[i][1] for i in range(num_row)}

letter_len = 0


def number_to_letter(n):
    '''

    :param n: input integer n from 1 to 1000 inclusive
    :return: length of letter

    '''

    s = str(n)  # manipulating each digit of the number n
    letter = ''

    while len(s) > 0:

        if len(s) == 4:  # thousand
            letter = letter + data_dic[s[0]] + data_dic['1000']
            s = s[1:]


        elif len(s) == 3 and s[0] != '0':  # hundred
            letter = letter + data_dic[s[0]] + data_dic['100']

            if int(s) % 100 > 0:
                letter += 'and'

            s = s[1:]

        elif len(s) == 3 and s[0] == '0':  # hundred

            if int(s) % 100 > 0:
                letter += 'and'

            s = s[1:]

        elif len(s) == 2 and s[0] != '1':
            letter += data_dic[s[0] + '0']
            s = s[1:]

        elif len(s) == 2 and s[0] == '1':
            letter += data_dic[s]
            break

        elif len(s) == 1:
            letter += data_dic[s[0]]
            s = s[1:]

        else:
            print('bug in digit')

    return letter

print(number_to_letter(1443))
#  print(sum([len(number_to_letter(i)) for i in range(1, 1001)]))