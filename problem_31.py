def otways(amount):
    return amount//2 + 1  # when giving 1 p only, w=1 but for 1p and 2p,

def otfways(amount):
    return sum(otways(amount - 5 * five) for five in range(amount//5+1))

def otftways(amount):
    return sum(otfways(amount - 10 * ten) for ten in range(amount//10+1))

def otfttways(amount):
    return sum(otftways(amount - 20 * twenty) for twenty in range(amount//20+1))

def otfttfways(amount):
    return sum(otfttways(amount - 50 * fifty) for fifty in range(amount//50+1))

def otfttfpways(amount):
    return sum(otfttfways(amount - 100 * pound) for pound in range(amount//100+1))

def otfttfptpways(amount):
    return sum(otfttfpways(amount - 200 * two_pounds) for two_pounds in range(amount//200+1))

print(otfttfptpways(1000))

