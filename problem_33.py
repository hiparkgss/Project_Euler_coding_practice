import decimal as dc

result = []
for i in range(10, 100):
    # print('i is', i)
    for j in range(i+1, 100):
        # print('j is ', j)
        for digit in str(i):
            if digit in str(j) and digit is not '0':
                # print('digit is ', digit)
                frac = dc.Decimal(i) / dc.Decimal(j)
                # print('frac is ', frac)
                if not dc.Decimal(int(str(j).replace(digit, '', 1))) == 0:
                    if frac == dc.Decimal(int(str(i).replace(digit, '', 1)))/dc.Decimal(int(str(j).replace(digit, '', 1))):
                        result.append([i, j])

print(result)
