import sys

pentagonals = set()
for n in range(1, 10000):
    pent = n * (3 * n - 1) / 2
    pentagonals.add(pent)

    for pent2 in pentagonals:
        if pent - pent2 in pentagonals:
            pent3 = pent - pent2
            if abs(pent2 - pent3) in pentagonals:
                print(pent2, pent3, abs(pent2 - pent3))
                sys.exit()

# list is slower than set/dictionary in terms of 'in ' command
# because list also has information about index while set/dictionary do not.