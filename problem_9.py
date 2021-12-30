for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        diff = c ** 2 - a ** 2 - b ** 2
        if diff == 0:
            print([a,b,c], a * b * c)
